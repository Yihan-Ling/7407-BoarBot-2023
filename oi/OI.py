from robotpy_toolkit_7407.utils import logger
import constants
from oi.keymap import Keymap
from robot_systems import Robot, Sensors, Pneumatics
logger.info("Hi, I'm OI!")


class OI:
    @staticmethod
    def init() -> None:
        logger.info("Initializing OI...")

    @staticmethod
    def map_controls():
        logger.info("Mapping controls...")
        pass

    def driveStyle():
        if constants.driveType == "arcade":
            constants.driveType = "tank"
            print(constants.driveType)
            return
        if constants.driveType == "tank":
            constants.driveType = "diff"
            print(constants.driveType)
            return
        if constants.driveType == "diff":
            constants.driveType = "arcade"
            print(constants.driveType)
            return

    Keymap.Drivetrain.DRIVE_STYLE().whenPressed(driveStyle)