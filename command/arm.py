import commands2
import config
import ctre
from subsystem import Drivetrain
from robotpy_toolkit_7407.command import SubsystemCommand
from oi.keymap import Keymap
from robot_systems import Robot
# from sensors import Pigeon2
import constants

class drivetrainCostum(commands2.CommandBase):

    def __init__(self, subsystem: Drivetrain) -> None:
        super().__init__()
        self.subsystem = subsystem

    def initialize(self) -> None:
        pass


    def execute(self) -> None:

        def deadZone(value):
            if value < -0.15 or value > 0.15:
                return value
            else:
                return 0

        print(Pigeon2.get_absolute_robot_heading())    

        if constants.driveType == "tank":
            left = Keymap.Drivetrain.LEFT_AXIS_Y.value
            right = Keymap.Drivetrain.RIGHT_AXIS_Y.value
            self.subsystem.left.setSpeed(deadZone(-left))
            self.subsystem.right.setSpeed(deadZone(right))
        if constants.driveType == "arcade":
            movement = Keymap.Drivetrain.LEFT_AXIS_Y.value
            rotation = Keymap.Drivetrain.LEFT_AXIS_X.value
            self.subsystem.left.setSpeed(deadZone(-movement + rotation))
            self.subsystem.right.setSpeed(deadZone(movement + rotation))
        if constants.driveType == "diff":
            movement = Keymap.Drivetrain.LEFT_AXIS_Y.value
            rotation = Keymap.Drivetrain.RIGHT_AXIS_X.value
            self.subsystem.left.setSpeed(deadZone(-movement + rotation))
            self.subsystem.right.setSpeed(deadZone(movement + rotation))

    def end(self, interrupted) -> None:
        pass

    def isFinished(self) -> bool:
        return False

    def runsWhenDisabled(self) -> bool:
        return False
