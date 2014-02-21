"""
QuickBot wiring config.

Specifies which pins are used for motor control, IR sensors and wheel encoders.
"""

# Motor pins: (dir1_pin, dir2_pin, pwd_pin)
RIGHT_MOTOR_PINS  = 'P8_12', 'P8_10', 'P9_14'
LEFT_MOTOR_PINS = 'P8_14', 'P8_16', 'P9_16'

# IR sensors (clock-wise, starting with the rear left sensor):
# rear-left, front-left, front, front-right, rear-right
IR_PINS = ('P9_38', 'P9_40', 'P9_36', 'P9_35', 'P9_33')

# Wheel encoder sensors: (left, right)
ENC_PINS = ('P9_39', 'P9_37')




