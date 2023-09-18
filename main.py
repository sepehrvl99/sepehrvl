import csv
import json
from typing import Optional
import pandas
import numpy

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<string:html_file>')
def home(html_file: Optional[str] = None):
    return render_template(html_file)


def write_to_csv(data):
    email = data['email']
    password = data['password']
    message = data['contact-message']
    with open('csv.csv', 'a') as csv_file:
        data = {
            'email': [email],
            'password': [password],
            'message': [message]
        }
        new_data = pandas.DataFrame(data).to_csv(index=False, header=False)

        csv_file.write(new_data)


@app.route('/submit_form', methods=['post', 'get'])
def submit_form():
    if request.method == 'POST':
        request_dict = request.form.to_dict()
        write_to_csv(request_dict)
        return 'Form submitted'

    else:
        return 'Somthing went wrong!'



