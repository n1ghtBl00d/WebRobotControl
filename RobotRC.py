import RPi.GPIO as GPIO
import numpy
import atexit


class RobotRC : 

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

        GPIO.setup(RobotRC.pinList, GPIO.OUT)

        atexit.register(RobotRC.endControl)
 

        return 0



    def update(axisX, axisY, tiltUp, tiltDown) :
        forward = 0
        backward = 0
        right = 0
        left = 0

        if(axisY > RobotRC.axisTolerance) :
            backward = 1
        elif(axisY < (RobotRC.axisTolerance * -1)) :
            forward = 1

        if(axisX > RobotRC.axisTolerance) :
            right = 1
        elif(axisX < (RobotRC.axisTolerance * -1)) :
            left = 1

        if(tiltUp == 1) :
            RobotRC.tilt = 1
        if(tiltDown == 1) :
            RobotRC.tilt = 0
        GPIO.output(RobotRC.fPin, forward)
        GPIO.output(RobotRC.bPin, backward)
        GPIO.output(RobotRC.rPin, right)
        GPIO.output(RobotRC.lPin, left)
        GPIO.output(RobotRC.tiltPin, RobotRC.tilt)

        return 0

    def stop() :

        GPIO.output(RobotRC.pinList, 0)


    def endControl() :
        
        GPIO.cleanup()

        return 0
