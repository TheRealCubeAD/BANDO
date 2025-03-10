
# ds3231_port_test

# Test/demo of portable driver for DS3231 precision RTC chip



# Author: Peter Hinch

# Copyright Peter Hinch 2018 Released under the MIT license



from machine import Pin, I2C

import utime

import sys

from clock import DS3231



# A Pyboard test

#from pyb import RTC

#rtc = RTC()

#rtc.datetime((2018, 1, 1, 1, 12, 0, 0, 0))  # Force incorrect setting



# mode and pull are specified in case pullups are absent.

# The pin ID's are arbitrary.

if sys.platform == 'pyboard':

    scl_pin = Pin('X2', pull=Pin.PULL_UP, mode=Pin.OPEN_DRAIN)

    sda_pin = Pin('X1', pull=Pin.PULL_UP, mode=Pin.OPEN_DRAIN)

else:  # I tested on ESP32

    scl_pin = Pin(5, pull=Pin.PULL_UP, mode=Pin.OPEN_DRAIN)

    sda_pin = Pin(4, pull=Pin.PULL_UP, mode=Pin.OPEN_DRAIN)



i2c = I2C(-1, scl=scl_pin, sda=sda_pin)

ds3231 = DS3231(i2c)



print('Initial values')

print('DS3231 time:', ds3231.get_time())

print('RTC time:   ', utime.localtime())



print('Setting DS3231 from RTC')

ds3231.save_time()  # Set DS3231 from RTC

print('DS3231 time:', ds3231.get_time())

print('RTC time:   ', utime.localtime())



print('Running RTC test for 2 mins')

print('RTC leads DS3231 by', ds3231.rtc_test(120, True), 'ppm')