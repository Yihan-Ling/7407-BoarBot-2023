import commands2
import wpilib

# import autonomous
import command
import config
import constants
import robot_systems
import sensors
import subsystem
import utils
from oi.OI import OI

from robot_systems import Robot
from oi.keymap import Keymap

class _Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()

    def robotInit(self):
        # Initialize Operator Interface
        OI.init()
        OI.map_controls()

    def robotPeriodic(self) -> None:
        commands2.CommandScheduler.getInstance().run()

    # Initialize subsystems

    # Pneumatics

    def teleopInit(self):
        commands2.CommandScheduler.getInstance().schedule(command.drivetrainCustom(Robot.drivetrain))

    def teleopPeriodic(self):

        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        
        pass

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(_Robot)
