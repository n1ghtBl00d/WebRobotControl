from crypt import methods
from urllib import response
from flask import Flask, render_template, request, redirect, url_for, make_response
import socket
#from RobotRC import RobotRC as RobotControl
from RobotTank import RobotTank as RobotControl

RobotControl.setup()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/gamepad', methods=['POST'])
def interpretControls():
    
    # Axes for Arcade/Balancing
    # axisX = request.json['axisX']
    # axisY = request.json['axisY']
    axisL = request.json['axisL']
    axisR = request.json['axisR']
    # buttonUp = request.json['buttonUp']
    # buttonDown = request.json['buttonDown']

    # RobotControl.update(axisX, axisY, buttonUp, buttonDown)
    RobotControl.update(axisL, axisR)

    response = make_response(redirect(url_for('index')))
    return(response)
    
@app.route('/stop', methods=['POST'])
def stopRobot():

    RobotControl.stop()

    response = make_response(redirect(url_for('index')))
    return(response)