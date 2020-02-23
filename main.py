import os

from flask import Flask, render_template, request, redirect, url_for, session
from peewee import DoesNotExist
from model import Donation, Donor

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('all'))


@app.route('/donations/', methods=['GET'])
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/create', methods=['GET', 'POST'])
def create_donation():
    if request.method == 'POST':
        try:
            donor = Donor.get(name=request.form['name'])
            Donation.create(value=request.form['donation'], donor=donor)
            return redirect(url_for('home'))
        except DoesNotExist:
            return render_template('create.jinja2', error='User does not exist')
    else:
        return render_template('create.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)

