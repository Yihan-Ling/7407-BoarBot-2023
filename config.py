import ctre

'''
TODO: 
 * Change the ESC depends on what we are using
 - determined VictorSPX √

 * Change the ESC port numbers to what we are using

'''



class gearbox:

    class left:
        motorLeft_CAN = ctre.VictorSPX(0)
        motorRight_CAN = ctre.VictorSPX(1)

    class right:
        motorLeft_CAN = ctre.VictorSPX(3)
        motorRight_CAN = ctre.VictorSPX(4)


class CIM:

    class arm:
        motor_CAN = ctre.VictorSPX(5)