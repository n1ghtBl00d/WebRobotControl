from crypt import methods
from urllib import response
from flask import Flask, render_template, request, redirect, url_for, make_response, Response
from flask_socketio import SocketIO
#from RobotRC import RobotRC as RobotControl
#from RobotTank import RobotTank as RobotControl
from RobotArcade import RobotArcade as RobotControl
import cv2

RobotControl.setup()

app = Flask(__name__)
socketio = SocketIO(app)

camera = cv2.VideoCapture(-1)
enableCamera = 1

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

@socketio.on('Stop')
def handleStop(data):
    RobotControl.stop()

@socketio.on('robotControl')
def handleControl(data):
    #print(data)
    RobotControl.update(data['axisL'], data['axisR'])


@app.route('/video_feed')
def video_feed():
    return Response(genFrame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def genFrame():
    global enableCamera
    while enableCamera:
        print("Camera")
        success, frame = camera.read()
        if not success:
            break
        else:

            scale = 50
            width = int(frame.shape[1] * scale / 100)
            height = int(frame.shape[0] * scale / 100)
            dim = (width, height)

            resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

            ret, buffer = cv2.imencode('.jpg', resized)
            newFrame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + newFrame + b'\r\n')