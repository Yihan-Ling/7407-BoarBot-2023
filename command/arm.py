import commands2
import config
import ctre
from subsystem import Arm
from robotpy_toolkit_7407.command import SubsystemCommand
from oi.keymap import Keymap
from robot_systems import Robot
# from sensors import Pigeon2
import constants

'''
TODO: Change the arm direction and speed accordingly 
'''
class armMove(commands2.CommandBase):

    def __init__(self, direction, subsystem: Arm):
        super().__init__()
        self.subsystem = subsystem
        self.direction = direction

    def initialize(self) -> None:
        pass

    def execute(self):
        Arm.motor.setSpeed(self.direction*0.5)

    def end(self, interrupted):
        Arm.motor.setSpeed(0)

    def isFinished(self):
        return False
        # return the button is pressed 

    
