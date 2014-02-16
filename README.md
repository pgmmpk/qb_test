# QuickBot tests

## Introduction

These are tests for QuickBot motors, IR sensors and wheel encoders.

QuickBot is a simple wheeled robot, built as part of (Coursera "Control of Mobile Robots"
class)[https://class.coursera.org/conrob-002]. It uses BeagleBone Black ARM-based mini-computer
as its "brains".

These tests have to be run on the QuickBot side. These tests directly "talk" to BeagleBone hardware.

### Install required libraries

    opkg install python-misc

### Clone qb_test git repository

    git clone https://github.com/pgmmpk/qb_test.git

## Running tests

### qt_test_motor

Tests motor wiring by running each motor in each direction. This test runs for about 30 seconds total
and does the following:

1. Runs left motor _forward_ for about 5 seconds and then stops
2. Runs left motor _in reverse_ for about 5 seconds and then stops
3. Runs right motor _forward_ for about 5 seconds and then stops
4. Runs right motor _in reverse_ for about 5 seconds and stops

Start it like this:

    python qb_test_motor.py

### qt_test_ir

Tests IR sensor wiring by printing IR readings for about 30 seconds. You can use your hand to simulate "an obstacle"
in front of each IR sensor and see how readings change. Unobstructed reading is low (zero). If you place an obstacle in
front of a sensor, reading should be high (approximately 300-800).

Start it like this:

    python qb_test_ir.py

### qt_test_encoder

Tests wheel encoder wiring by reading values for about 30 seconds and printing them out. Manually rotate each wheel
to see encoders generate periodic pattern. Note that encoder readings are very noisy, they may fluctuate even
when wheels are not moved. However, rotating wheels should give you much larger amplitude of change.

Start it like this:

    python qb_test_encoder.py


## License
MIT
