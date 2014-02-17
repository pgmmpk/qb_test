"""
Mike Kroutikov, (c) 2014

Researching QuickBot wheel encoder.

Run this code on the BeagleBone side.

It will grab few seconds seconds of raw wheel encoder readings and write the result as
a CSV file. You can import it into a spreadsheet software like Excel and analyze it (e.g. plot it).
"""
import Adafruit_BBIO.ADC as ADC
import time
import numpy as np


def write_csv(filename, buf):
    """
    Writes numpy array as a CSV file.
    Numpy array is assumed to have 2 dimensions: (rows, cols)
    """
    rows, cols = buf.shape

    with open(filename, 'wb') as f:
        for i in range(rows):
            s = ', '.join(str(x) for x in buf[i, :]) + '\n'
            f.write(s.encode('utf-8'))

if __name__ == '__main__':
    import config

    NUM_SAMPLES = 3000 # 5-10 seconds of data
    filename = 'data.csv'

    size = NUM_SAMPLES
    buf = np.zeros((size, len(config.ENC_PINS)), dtype=np.int)

    print "Grabbing wheel encoder readings and saving to", filename
    print "Try manually rotating wheels to see the effect in the data"

    ADC.setup()

    for i in range(size):
        values = tuple(ADC.read_raw(pin) for pin in config.ENC_PINS)
        #print('Raw encoder values: %4d  %4d' % values)
        buf[i, 0] = values[0]
        buf[i, 1] = values[1]
        time.sleep(0.001)

    print "Done grabbing. Writing data out as ", filename
    write_csv(filename, buf)
    print "Done"
