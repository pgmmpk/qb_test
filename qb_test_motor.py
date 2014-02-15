#!/usr/bin/python
"""
@brief QuickBotTest class for Beaglebone Black

@author Rowland O'Flaherty (rowlandoflaherty.com)
@author Mike Kroutikov (pgmmpk@gmail.com) - adapted Rowland's code for local tests of Bot sensors and actuators
@date 02/07/2014
@version: 1.0
@copyright: Copyright (C) 2014, Georgia Tech Research Corporation see the LICENSE file included with this software (see LINENSE file)
"""
import contextlib
import time


import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC

@contextlib.contextmanager
def motor_setup(dir1_pin, dir2_pin, pwm_pin):
    # Initialize GPIO pins
    GPIO.setup(dir1_pin, GPIO.OUT)
    GPIO.setup(dir2_pin, GPIO.OUT)

    # Initialize PWM pins: PWM.start(channel, duty, freq=2000, polarity=0)
    PWM.start(pwm_pin, 0)

    def run(speed):
        if speed > 100:
            speed = 100
        elif speed < -100:
            speed = -100

        if speed > 0:
            GPIO.output(dir1_pin, GPIO.LOW)
            GPIO.output(dir2_pin, GPIO.HIGH)
            PWM.set_duty_cycle(pwm_pin, abs(speed))
        elif speed < 0:
            GPIO.output(dir1_pin, GPIO.HIGH)
            GPIO.output(dir2_pin, GPIO.LOW)
            PWM.set_duty_cycle(pwm_pin, abs(speed))
        else:
            GPIO.output(dir1_pin, GPIO.LOW)
            GPIO.output(dir2_pin, GPIO.LOW)
            PWM.set_duty_cycle(pwm_pin, 0)

    yield run

    GPIO.cleanup()
    PWM.cleanup()

def x(enc_pin):
    ADC.setup()

    for _ in range(20):
        ADC.read_raw(enc_pin)

if __name__ == '__main__':

    LEFT_MOTOR_PINS = 'P8_12', 'P8_10', 'P9_14'
    RIGHT_MOTOR_PINS = 'P8_14', 'P8_16', 'P9_16'

    print('====== Testing Quick Bot =======')

    print()
    print('Left motor should follow commands')
    print()

    with motor_setup(*LEFT_MOTOR_PINS) as run:
        print('Left motor: Run forward')
        run(50)
        time.sleep(5)

        print('Left motor: Stop')
        run(0)
        time.sleep(2)

        print('Left motor: Run backwards')
        run(-50)
        time.sleep(5)

        print('Left motor: Stop')
        run(0)

        print('\tForward')

    print()
    print('Right motor should follow commands')
    print()

    with motor_setup(*RIGHT_MOTOR_PINS) as run:
        print('Right motor: Run forward')
        run(50)
        time.sleep(5)

        print('Right motor: Stop')
        run(0)
        time.sleep(2)

        print('Right motor: Run backwards')
        run(-50)
        time.sleep(5)

        print('Right motor: Stop')
        run(0)

        print('\tForward')
