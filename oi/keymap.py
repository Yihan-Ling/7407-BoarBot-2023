from robotpy_toolkit_7407.oi import (
    XBoxController,
    LogitechController,
    JoystickAxis,
    DefaultButton,
)

DriverCONTROLLER = XBoxController

class Controllers:
    DRIVER = 0
    OPERATOR: int


class Keymap:
    class Drivetrain:
        # Left_Wheels_Speed = JoystickAxis(Controllers.DRIVER, DriverCONTROLLER.L_JOY[1])
        # if (Left_Wheels_Speed < 0.2 and Left_Wheels_Speed > -0.2):
        #     Left_Wheels_Speed=0

        # Right_Wheels_Speed = JoystickAxis(Controllers.DRIVER, DriverCONTROLLER.R_JOY[1])
        # if (Right_Wheels_Speed < 0.2 and Right_Wheels_Speed > -0.2):
        #     Right_Wheels_Speed=0
        LEFT_AXIS_Y = JoystickAxis(Controllers.DRIVER, DriverCONTROLLER.L_JOY[1])
        LEFT_AXIS_X = JoystickAxis(Controllers.DRIVER, DriverCONTROLLER.L_JOY[0])
        RIGHT_AXIS_Y = JoystickAxis(Controllers.DRIVER, DriverCONTROLLER.R_JOY[1])
        RIGHT_AXIS_X = JoystickAxis(Controllers.DRIVER, DriverCONTROLLER.R_JOY[0])
        DRIVE_STYLE = DefaultButton(Controllers.DRIVER, DriverCONTROLLER.SELECT)
        CENTRIC = DefaultButton(DriverCONTROLLER, DriverCONTROLLER.START)
        RESET_GYRO = DefaultButton(DriverCONTROLLER, DriverCONTROLLER.A)
    pass
