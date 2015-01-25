import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    if (GPIO.input(24) ==0):
        os.system("python /home/pi/pythoncode/picameraTrigger_2.py")

        
### to add for autorun:
### $ sudo nano / etc/rc.local
### at the bottom, just above exit 0 add: python /home/pi/pythoncode/run.py
