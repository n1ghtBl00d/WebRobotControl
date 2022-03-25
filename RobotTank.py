import gpiozero as gpio

class RobotTank:
    
    lMotorA = "BOARD11"
    lMotorB = "BOARD12"
    lMotorEN = "BOARD13"

    rMotorA = "BOARD15"
    rMotorB = "BOARD16"
    rMotorEN = "BOARD18"

    #lMotor.motor = -1
    #rMotor.motor = -1

    robot = -1

    axisDeadzone = 0.35

    def setup():
        #lMotor.motor = gpio.Motor(forward = lMotorA, backward= lMotorB)
        #rMotor.motor = gpio.Motor(forward = rMotorA, backward= rMotorB)

        RobotTank.robot = gpio.Robot(left=(RobotTank.lMotorA, RobotTank.lMotorB, RobotTank.lMotorEN), right=(RobotTank.rMotorA, RobotTank.rMotorB, RobotTank.rMotorEN))

    def update(axisL, axisR):

        if (abs(axisL) < RobotTank.axisDeadzone):
            axisL = 0
        if (abs(axisR) < RobotTank.axisDeadzone):
            axisR = 0
        
        RobotTank.robot.value = (axisL, axisR)

    def stop():
        RobotTank.robot.value = (0,0)

    def endControl():
        gpio.close()
