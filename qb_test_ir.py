"""
Mike Kroutikov, (c) 2014

Test QuickBot IR sensors.

Run this code on the BeagleBone side.

It will display for about 30 seconds the current values of all five sensors.

While this program runs, try putting an obstacle before each sensor. Unobstructed sensor should read
low value (e.g. 0). Placing palm of your hand at about 2 inches should cause large readings (300-700).

"""
import Adafruit_BBIO.ADC as ADC
import time

if __name__ == '__main__':
    import config

    print("Testing IR sensors. Try putting hand in front of a sensor to see its value change")

    ADC.setup()

    for _ in range(60):
        values = tuple(ADC.read_raw(pin) for pin in config.IR_PINS)
	time.sleep(0.5)
        print('Raw sensor values: %4d %4d %4d %4d %4d' % values)

    print("Done")
