# 60s countdown (starts at 59 and ends at zero)
from microbit import *
import time


def set_0(brightness):
    display.set_pixel(1, 0, brightness)
    display.set_pixel(2, 0, brightness)
    display.set_pixel(0, 1, brightness)
    display.set_pixel(0, 2, brightness)
    display.set_pixel(0, 3, brightness)
    display.set_pixel(1, 4, brightness)
    display.set_pixel(2, 4, brightness)
    display.set_pixel(3, 3, brightness)
    display.set_pixel(3, 2, brightness)
    display.set_pixel(3, 1, brightness)


def set_1(brightness):
    display.set_pixel(1, 1, brightness)
    display.set_pixel(2, 0, brightness)
    display.set_pixel(2, 1, brightness)
    display.set_pixel(2, 2, brightness)
    display.set_pixel(2, 3, brightness)
    display.set_pixel(2, 4, brightness)
    display.set_pixel(1, 4, brightness)
    display.set_pixel(3, 4, brightness)


def set_2(brightness):
    display.set_pixel(0, 1, brightness)
    display.set_pixel(1, 0, brightness)
    display.set_pixel(2, 0, brightness)
    display.set_pixel(3, 1, brightness)
    display.set_pixel(2, 2, brightness)
    display.set_pixel(1, 3, brightness)
    display.set_pixel(0, 4, brightness)
    display.set_pixel(1, 4, brightness)
    display.set_pixel(2, 4, brightness)
    display.set_pixel(3, 4, brightness)


def set_3(brightness):
    display.set_pixel(0, 1, brightness)
    display.set_pixel(1, 0, brightness)
    display.set_pixel(2, 0, brightness)
    display.set_pixel(3, 1, brightness)
    display.set_pixel(2, 2, brightness)
    display.set_pixel(3, 3, brightness)
    display.set_pixel(2, 4, brightness)
    display.set_pixel(1, 4, brightness)
    display.set_pixel(0, 3, brightness)


def set_4(brightness):
    display.set_pixel(2, 0, brightness)
    display.set_pixel(1, 1, brightness)
    display.set_pixel(1, 2, brightness)
    display.set_pixel(3, 2, brightness)
    display.set_pixel(2, 2, brightness)
    display.set_pixel(3, 0, brightness)
    display.set_pixel(3, 1, brightness)
    display.set_pixel(3, 3, brightness)
    display.set_pixel(3, 4, brightness)


def set_5(brightness):
    display.set_pixel(0, 0, brightness)
    display.set_pixel(1, 0, brightness)
    display.set_pixel(2, 0, brightness)
    display.set_pixel(3, 0, brightness)
    display.set_pixel(0, 1, brightness)
    display.set_pixel(0, 2, brightness)
    display.set_pixel(1, 2, brightness)
    display.set_pixel(2, 2, brightness)
    display.set_pixel(3, 3, brightness)
    display.set_pixel(2, 4, brightness)
    display.set_pixel(1, 4, brightness)
    display.set_pixel(0, 4, brightness)


def set_6(brightness):
    display.set_pixel(2, 0, brightness)
    display.set_pixel(1, 1, brightness)
    display.set_pixel(0, 2, brightness)
    display.set_pixel(0, 3, brightness)
    display.set_pixel(1, 4, brightness)
    display.set_pixel(2, 4, brightness)
    display.set_pixel(3, 3, brightness)
    display.set_pixel(2, 2, brightness)
    display.set_pixel(1, 2, brightness)


def set_7(brightness):
    display.set_pixel(0, 0, brightness)
    display.set_pixel(1, 0, brightness)
    display.set_pixel(2, 0, brightness)
    display.set_pixel(3, 0, brightness)
    display.set_pixel(2, 1, brightness)
    display.set_pixel(1, 2, brightness)
    display.set_pixel(1, 3, brightness)
    display.set_pixel(1, 4, brightness)


def set_8(brightness):
    display.set_pixel(1, 0, brightness)
    display.set_pixel(2, 0, brightness)
    display.set_pixel(0, 1, brightness)
    display.set_pixel(3, 1, brightness)
    display.set_pixel(1, 2, brightness)
    display.set_pixel(2, 2, brightness)
    display.set_pixel(3, 3, brightness)
    display.set_pixel(0, 3, brightness)
    display.set_pixel(1, 4, brightness)
    display.set_pixel(2, 4, brightness)


def set_9(brightness):
    display.set_pixel(1, 0, brightness)
    display.set_pixel(2, 0, brightness)
    display.set_pixel(0, 1, brightness)
    display.set_pixel(3, 1, brightness)
    display.set_pixel(1, 2, brightness)
    display.set_pixel(2, 2, brightness)
    display.set_pixel(3, 2, brightness)
    display.set_pixel(3, 3, brightness)
    display.set_pixel(2, 4, brightness)
    display.set_pixel(1, 4, brightness)


def set_10(brightness):
    display.set_pixel(4,4,brightness)


def set_20(brightness):
    display.set_pixel(4,3,brightness)


def set_30(brightness):
    display.set_pixel(4,2,brightness)


def set_40(brightness):
    display.set_pixel(4,1,brightness)


def set_50(brightness):
    display.set_pixel(4,0,brightness)


def countdown():
    set_9(9)
    time.sleep(1)
    set_9(0)
    set_8(9)
    time.sleep(1)
    set_8(0)
    set_7(9)
    time.sleep(1)
    set_7(0)
    set_6(9)
    time.sleep(1)
    set_6(0)
    set_5(9)
    time.sleep(1)
    set_5(0)
    set_4(9)
    time.sleep(1)
    set_4(0)
    set_3(9)
    time.sleep(1)
    set_3(0)
    set_2(9)
    time.sleep(1)
    set_2(0)
    set_1(9)
    time.sleep(1)
    set_1(0)
    set_0(9)
    time.sleep(1)
    set_0(0)


while True:
    set_10(9)
    set_20(9)
    set_30(9)
    set_40(9)
    set_50(9)
    countdown()
    set_50(0)
    countdown()
    set_40(0)
    countdown()
    set_30(0)
    countdown()
    set_20(0)
    countdown()
    set_10(0)
    countdown()


