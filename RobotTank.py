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

        RobotZTank.robot = gpio.Robot(left=(RobotZTank.lMotorA, RobotZTank.lMotorB, RobotZTank.lMotorEN), right=(RobotZTank.rMotorA, RobotZTank.rMotorB, RobotZTank.rMotorEN))

    def update(axisL, axisR):

        if (abs(axisL) < RobotZTank.axisDeadzone):
            axisL = 0
        if (abs(axisR) < RobotZTank.axisDeadzone):
            axisR = 0
        
        RobotZTank.robot.value = (axisL, axisR)

    def stop():
        RobotZTank.robot.value = (0,0)

    def endControl():
        gpio.close()
