# from robotpy_toolkit_7407.motors.rev_motors import SparkMax
from commands2 import Subsystem
import ctre
import config

class CIM():

    def __init__(self, motor):
        self.motor = motor

    def setSpeed(self, percentage):
        self.motor.set(ctre.ControlMode.PercentOutput, percentage)


class Arm(Subsystem):
    
    motor = CIM(config.CIM.arm.motor_CAN)


