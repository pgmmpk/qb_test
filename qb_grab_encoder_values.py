'''
Mike Kroutikov, (c) 2014

Test QuickBot wheel encoder.

Run this code on the BeagleBone side.

It will grab 30 seconds of raw wheel encoder data and write it to local file for analysis.
'''
import Adafruit_BBIO.ADC as ADC
import time
import numpy as np


def write_csv(filename, buf):
    rows, cols = buf.shape

    with open(filename, 'wb') as f:
        for i in range(rows):
            s = ', '.join(buf[i, :]) + '\n'
            f.write(s.encode('utf-8'))

if __name__ == '__main__':
    import config

    NUM_SECS = 30 # 30 seconds of data
    DT = 0.001    # 1 millisec apart

    size = int(NUM_SECS / DT)
    buf = np.zeros((size, len(config.ENC_PINS)), dtype=np.int)

    print "Grabbing wheel encoder readings. Try manually rotating wheels to see how encoder values change"

    ADC.setup()

    for i in range(size):
        values = tuple(ADC.read_raw(pin) for pin in config.ENC_PINS)
        #print('Raw encoder values: %4d  %4d' % values)
        buffer[i, 0] = values[0]
        buffer[i, 1] = values[1]
        time.sleep(DT)

    print "Done grabbing. Writing data out"
    write_csv('encoder_grab.csv', buffer)
    print "Done"
