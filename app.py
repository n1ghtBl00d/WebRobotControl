from crypt import methods
from urllib import response
from flask import Flask, render_template, request, redirect, url_for, make_response, Response
from flask_socketio import SocketIO

import threading
import cv2
import base64

#from RobotArcade import RobotArcade as RobotControl
from RobotMecanum import RobotMecanum as RobotControl

RobotControl.setup()

app = Flask(__name__)
socketio = SocketIO(app)

enableCamera = 0





def cameraLoop(width = 640, height = 480):
    camera = cv2.VideoCapture(-1)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    camera.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75)

    while enableCamera:
        success, frame = camera.read()
        if success:
            ret, buffer = cv2.imencode('.jpg', frame)
            imgString = base64.b64encode(buffer)
            imgString = "data:image/jpg;base64," + imgString.decode('utf-8')
            socketio.emit("camera", {"imgString": imgString})
    camera.release()

cameraThread = threading.Thread(target=cameraLoop, daemon=True)

@app.route("/")
def index():
    return render_template('index.html')

@socketio.on('Stop')
def handleStop(data):
    RobotControl.stop()

@socketio.on('robotControl')
def handleControl(data):
    #print(data)
    RobotControl.update(data['axisLy'], data['axisLx'], data['axisRx'])

@socketio.on('startCamera')
def startCam(data):
    global enableCamera
    global cameraThread
    print("startCamera")
    enableCamera = 1
    if(cameraThread.is_alive() == False):
        cameraThread = threading.Thread(target=cameraLoop, daemon=True)
        cameraThread.start()

@socketio.on('stopCamera')
def startCam(data):
    global enableCamera
    print("stopCamera")
    enableCamera = 0






