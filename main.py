import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation 

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/create', methods=['GET', 'POST'])
def create_donation():
    if request.method == 'POST':
        Donation.create(value=request.form['donation'], donor=request.form['name'])
        redirect(url_for('home'))
    else:
        return render_template('create.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)

