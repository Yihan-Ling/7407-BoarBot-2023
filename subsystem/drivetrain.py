# from robotpy_toolkit_7407.motors.rev_motors import SparkMax
from commands2 import Subsystem
import ctre
import config

class gearbox():

    def __init__(self, leftMotor, rightMotor, side):
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        self.side = side
        self.rightMotor.follow(self.leftMotor)

    def setSpeed(self, percentage):
        self.leftMotor.set(ctre.ControlMode.PercentOutput, percentage)


class Drivetrain(Subsystem):
    left = gearbox(
        config.gearbox.left.motorLeft_CAN,
        config.gearbox.left.motorRight_CAN,
        "left"
    )

    right = gearbox(
        config.gearbox.right.motorLeft_CAN,
        config.gearbox.right.motorRight_CAN,
        "right"
    )


