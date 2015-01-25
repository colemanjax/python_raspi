# gray = rt btn_R; purple = LED+; gray = rt btn_L; white = lt btn_R; black = lt btn_L and resistor(->LED-)

import RPi.GPIO as GPIO
import time, os, picamera
from time import gmtime, strftime

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT) # GPIO17 for LED

while True:
    if(GPIO.input(24) == 0): # this would be the trigger input pin
        print("HIGH")
        GPIO.output(17,GPIO.HIGH)
        GPIO.wait_for_edge(23, GPIO.FALLING)
        print("LOW")
        GPIO.output(17,GPIO.LOW)
        break

    print("PRESS BTN TO STOP")
    
