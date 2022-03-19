import RPi.GPIO as GPIO
import numpy
import atexit


class RobotControl : 

    pwm = -1

    fPin = 3
    bPin = 5
    rPin = 11
    lPin = 13
    tiltPin = 8

    tilt = 0

    axisTolerance = 0.5

    pinList = [fPin,
               bPin,
               rPin,
               lPin,
               tiltPin]

    def setup() :

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(RobotControl.pinList, GPIO.OUT)

        atexit.register(RobotControl.endControl)
 

        return 0



    def update(axisX, axisY, tiltUp, tiltDown) :
        forward = 0
        backward = 0
        right = 0
        left = 0

        if(axisY > RobotControl.axisTolerance) :
            backward = 1
        elif(axisY < (RobotControl.axisTolerance * -1)) :
            forward = 1

        if(axisX > RobotControl.axisTolerance) :
            right = 1
        elif(axisX < (RobotControl.axisTolerance * -1)) :
            left = 1

        if(tiltUp == 1) :
            RobotControl.tilt = 1
        if(tiltDown == 1) :
            RobotControl.tilt = 0
        GPIO.output(RobotControl.fPin, forward)
        GPIO.output(RobotControl.bPin, backward)
        GPIO.output(RobotControl.rPin, right)
        GPIO.output(RobotControl.lPin, left)
        GPIO.output(RobotControl.tiltPin, RobotControl.tilt)

        return 0

    def stop() :

        GPIO.output(RobotControl.pinList, 0)


    def endControl() :
        
        GPIO.cleanup()

        return 0
