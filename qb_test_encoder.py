'''
Mike Kroutikov, (c) 2014

Test QuickBot wheel encoder.

Run this code on the BeagleBone side.

It will display for about 30 seconds the current values of wheel encoders.

While this program runs, try rotating wheels to see encoder values changing.

Note that values are pretty noisy, so expect some fluctuations even with static wheels.
'''
import Adafruit_BBIO.ADC as ADC
import time


def display_ranges(val1, val2):
    '''
    Display encoder values as pseudo-graphics bars, e.g.

    ***      | *****
    '''
    if val1 > 2048:
        val1 = 2048
    if val2 > 2048:
        val2 = 2048

    val1 = int(val1 / 256)
    val2 = int(val2 / 256)

    s = '*' * val1 + ' ' * (8 - val1) + ' | ' + '*' * val2 + ' ' * (8 - val2)

    print s


if __name__ == '__main__':
    import config

    print("Testing wheel encoders. Try manually rotating wheels to see how encoder values change")

    ADC.setup()

    for _ in range(600):
        values = tuple(ADC.read_raw(pin) for pin in config.ENC_PINS)
        #print('Raw encoder values: %4d  %4d' % values)
        display_ranges(*values)
        time.sleep(0.05)

    print("Done")
