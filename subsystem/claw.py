# from robotpy_toolkit_7407.motors.rev_motors import SparkMax
from commands2 import Subsystem
import ctre
import config

class BAG():

    def __init__(self, BAGMotor, side):
        self.BAGMotor = BAGMotor

    def setSpeed(self, percentage):
        self.BAGMotor.set(ctre.ControlMode.PercentOutput, percentage)


class Claw(Subsystem):
    
    motor = BAG(config.BAG.motor_CAN)


