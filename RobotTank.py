import RPi.GPIO as GPIO
import numpy
import atexit


class RobotTank : 

    lPin = 12
    rPin = 33

    lMotor = -1
    rMotor = -1

    axisDeadzone = 0.35

    pinList = [rPin, lPin]

    def setup() :

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(RobotTank.pinList, GPIO.OUT)

        RobotTank.lMotor = GPIO.PWM(RobotTank.lPin, 50)
        RobotTank.rMotor = GPIO.PWM(RobotTank.rPin, 50)

        RobotTank.lMotor.start(0)
        RobotTank.rMotor.start(0)

        atexit.register(RobotTank.endControl)
 

        return 0



    def update(axisL, axisR) :
        
        lDutyCycle = numpy.interp(axisL, [1, -1], [6.7, 7.3])
        rDutyCycle = numpy.interp(axisR, [1, -1], [6.7, 7.3])

        if (abs(axisL) < RobotTank.axisDeadzone) :
            RobotTank.lMotor.ChangeDutyCycle(0)
        else :
            RobotTank.lMotor.ChangeDutyCycle(lDutyCycle)
        if (abs(axisR) < RobotTank.axisDeadzone) :
            RobotTank.rMotor.ChangeDutyCycle(0)
        else :
            RobotTank.rMotor.ChangeDutyCycle(rDutyCycle)

        return 0

    def stop() :

        RobotTank.lMotor.ChangeDutyCycle(0)
        RobotTank.rMotor.ChangeDutyCycle(0)


    def endControl() :
        
        GPIO.cleanup()

        return 0
