
import Adafruit_BBIO.ADC as ADC
import time

def display_ranges(val1, val2):
	if val1 > 2048:
		val1 = 2048
	if val2 > 2048:
		val2 = 2048
	
	val1 = int(val1 / 256)
	val2 = int(val2 / 256)

	s = '*' * val1 + ' ' * (8 - val1) + ' | ' +  '*' * val2 + ' ' * (8 - val2)

	print s

if __name__ == '__main__':

    ENC_PINS = ('P9_39','P9_37')

    print("Testing wheel encoders. Try manually rotating wheels to see how encoder values change")

    ADC.setup()

    for _ in range(600):
        values = tuple(ADC.read_raw(pin) for pin in ENC_PINS)
        #print('Raw encoder values: %4d  %4d' % values)
	display_ranges(*values)
	time.sleep(0.05)

    print("Done")
