import gpiozero as gpio

class RobotArcade:
    
    lMotorA = "BOARD11"
    lMotorB = "BOARD12"
    lMotorEN = "BOARD13"

    rMotorA = "BOARD15"
    rMotorB = "BOARD16"
    rMotorEN = "BOARD18"

    #lMotor.motor = -1
    #rMotor.motor = -1

    robot = -1

    axisDeadzone = 0.25
    maxSpeed = 0.8
    inputMultiplierY = 0.6
    inputMultiplierX = 0.4

    def setup():
        #lMotor.motor = gpio.Motor(forward = lMotorA, backward= lMotorB)
        #rMotor.motor = gpio.Motor(forward = rMotorA, backward= rMotorB)

        RobotArcade.robot = gpio.Robot(left=(RobotArcade.lMotorA, RobotArcade.lMotorB, RobotArcade.lMotorEN), right=(RobotArcade.rMotorA, RobotArcade.rMotorB, RobotArcade.rMotorEN))

    def update(axisY, axisX):

        if (abs(axisY) < RobotArcade.axisDeadzone):
            axisY = 0
        if (abs(axisX) < RobotArcade.axisDeadzone):
            axisX = 0

        axisY = axisY * RobotArcade.inputMultiplierY
        axisX = axisX * RobotArcade.inputMultiplierX
        
        valL = axisY - axisX
        valR = axisY + axisX

        if(valL > RobotArcade.maxSpeed) :
            valL = RobotArcade.maxSpeed
        if(valR > RobotArcade.maxSpeed) :
            valR = RobotArcade.maxSpeed
        if(valL < -RobotArcade.maxSpeed) :
            valL = -RobotArcade.maxSpeed
        if(valR < -RobotArcade.maxSpeed) :
            valR = -RobotArcade.maxSpeed

        RobotArcade.robot.value = (valL, valR)

    def stop():
        RobotArcade.robot.value = (0,0)

    def endControl():
        gpio.close()
