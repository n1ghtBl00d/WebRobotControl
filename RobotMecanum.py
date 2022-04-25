import gpiozero as gpio

class RobotMecanum:
    
    frMotorA = "BOARD11"
    frMotorB = "BOARD12"
    frMotorEN = "BOARD13"

    brMotorA = "BOARD15"
    brMotorB = "BOARD16"
    brMotorEN = "BOARD18"

    flMotorA = "BOARD37"
    flMotorB = "BOARD38"
    flMotorEN = "BOARD40"

    blMotorA = "BOARD31"
    blMotorB = "BOARD32"
    blMotorEN = "BOARD33"


    frontRobot = -1
    backRobot = -1

    axisDeadzone = 0.25
    maxSpeed = .8
    inputMultiplierY = .8
    inputMultiplierX = .5
    inputMultiplierRotate = .5

    def setup():
        #lMotor.motor = gpio.Motor(forward = lMotorA, backward= lMotorB)
        #rMotor.motor = gpio.Motor(forward = rMotorA, backward= rMotorB)

        RobotMecanum.frontRobot = gpio.Robot(left=(RobotMecanum.flMotorA, RobotMecanum.flMotorB, RobotMecanum.flMotorEN), right=(RobotMecanum.frMotorA, RobotMecanum.frMotorB, RobotMecanum.frMotorEN))
        RobotMecanum.backRobot = gpio.Robot(left=(RobotMecanum.blMotorA, RobotMecanum.blMotorB, RobotMecanum.blMotorEN), right=(RobotMecanum.brMotorA, RobotMecanum.brMotorB, RobotMecanum.brMotorEN))

    def update(axisLy, axisLx, axisRx):

        if (abs(axisLy) < RobotMecanum.axisDeadzone):
            axisLy = 0
        if (abs(axisLx) < RobotMecanum.axisDeadzone):
            axisLx = 0
        if (abs(axisRx) < RobotMecanum.axisDeadzone):
            axisRx = 0

        axisLy = axisLy * RobotMecanum.inputMultiplierY
        axisLx = axisLx * RobotMecanum.inputMultiplierX
        axisRx = axisRx * RobotMecanum.inputMultiplierRotate
        
        valFL = axisLx + axisRx - axisLy
        valFR = axisLx - axisRx - axisLy
        valBL = axisLx - axisRx + axisLy
        valBR = axisLx + axisRx + axisLy

        if(valFL > RobotMecanum.maxSpeed) :
            valFL = RobotMecanum.maxSpeed
        if(valFR > RobotMecanum.maxSpeed) :
            valFR = RobotMecanum.maxSpeed
        if(valFL < -RobotMecanum.maxSpeed) :
            valFL = -RobotMecanum.maxSpeed
        if(valFR < -RobotMecanum.maxSpeed) :
            valFR = -RobotMecanum.maxSpeed
        if(valBL > RobotMecanum.maxSpeed) :
            valBL = RobotMecanum.maxSpeed
        if(valBR > RobotMecanum.maxSpeed) :
            valBR = RobotMecanum.maxSpeed
        if(valBL < -RobotMecanum.maxSpeed) :
            valBL = -RobotMecanum.maxSpeed
        if(valBR < -RobotMecanum.maxSpeed) :
            valBR = -RobotMecanum.maxSpeed

        RobotMecanum.frontRobot.value = (valFL, valFR)
        RobotMecanum.backRobot.value = (valBL, valBR)

    def stop():
        RobotMecanum.frontRobot.value = (0,0)
        RobotMecanum.backRobot.value = (0,0)

    def endControl():
        gpio.close()
