import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) # GPIO17 for LED

GPIO.output(17,GPIO.HIGH)
time.sleep(10)
GPIO.output(17,GPIO.LOW)

GPIO.cleanup()

## *********

##GPIO.setmode(GPIO.BCM)
##GPIO.setup(17, GPIO.OUT) # GPIO17 for LED
##GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
##
##while True:
##    GPIO.wait_for_edge(24,GPIO.FALLING)
##    GPIO.output(17, GPIO.HIGH)
##    GPIO.wait_for_edge(24,GPIO.RISING)
##    GPIO.output(17, GPIO.LOW)
##    
##GPIO.cleanup()
