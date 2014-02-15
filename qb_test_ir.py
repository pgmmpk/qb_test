
import Adafruit_BBIO.ADC as ADC
import time

if __name__ == '__main__':

    IR_PINS = ('P9_38', 'P9_40', 'P9_36', 'P9_35', 'P9_33')

    print("Testing IR sensors. Try putting hand in front of a sensor to see its value change")

    ADC.setup()

    for _ in range(60):
        values = tuple(ADC.read_raw(pin) for pin in IR_PINS)
	time.sleep(0.5)
        print('Raw encoder values: %4d %4d %4d %4d %4d' % values)

    print("Done")
