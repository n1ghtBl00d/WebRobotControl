from urllib import response
from flask import Flask, render_template, request, redirect, url_for, make_response
import socket

from simplejson import JSONDecoder


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/gamepad', methods=['POST'])
def doStuff():
    
    print(request.json)


    response = make_response(redirect(url_for('index')))
    return(response)
    