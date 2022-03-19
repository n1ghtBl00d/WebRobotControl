from crypt import methods
from urllib import response
from flask import Flask, render_template, request, redirect, url_for, make_response
import socket
from control import RobotControl

RobotControl.setup()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/gamepad', methods=['POST'])
def interpretControls():
    
    axisX = request.json['axisX']
    axisY = request.json['axisY']
    buttonUp = request.json['buttonUp']
    buttonDown = request.json['buttonDown']

    RobotControl.update(axisX, axisY, buttonUp, buttonDown)

    response = make_response(redirect(url_for('index')))
    return(response)
    
@app.route('/stop', methods=['POST'])
def stopRobot():

    RobotControl.stop()

    response = make_response(redirect(url_for('index')))
    return(response)