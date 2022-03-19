from urllib import response
from flask import Flask, render_template, request, redirect, url_for, make_response
import socket


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def doStuff():
    print(request.form["test"])
    response = make_response(redirect(url_for('index')))
    return(response)
    