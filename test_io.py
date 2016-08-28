import CHIP_IO.GPIO as GPIO
import time


my_port = ['XIO-P0','XIO-P1']

for a in my_port:
    GPIO.setup(a, GPIO.OUT)

def turn_on(p):
    GPIO.output(p,1)


def turn_off(p):
    GPIO.output(p,0)


while True:
    time.sleep(1)
    turn_on(my_port[0])
    turn_off(my_port[1])
    time.sleep(1)
    turn_on(my_port[1])
    turn_off(my_port[0])



GPIO.cleanup()