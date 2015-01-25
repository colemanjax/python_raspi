#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# pir_1.py
# Detect movement using a PIR module
#
# Author : Matt Hawkins
# Date   : 21/01/2013

# Import required Python libraries
import RPi.GPIO as GPIO
import time, subprocess

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR = 7

new_path = "/home/pi/picam_tests/test2/"

print "PIR Module Test (CTRL-C to exit)"

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

Current_State  = 0
Previous_State = 0

try:

  print "Waiting for PIR to settle ..."

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    

  print "  Ready"     
    
  # Loop until users quits with CTRL-C
  while True :
   
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
   
    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print "  PHOTO BOOTH ON!"
      time.sleep(2)
      # run some other python script
      subprocess.Popen("python picameraBooth_1.py 1", shell = True)
      # Record previous state
      Previous_State=1
      time.sleep(13)
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "  Ready"
      Previous_State=0
      
    # Wait for 10 milliseconds
    time.sleep(0.01)      
      
except KeyboardInterrupt:
  from subprocess import call
  photofile = "sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh -s upload "+new_path+" /Apps/ColemanPiUploader/"
  call ([photofile], shell=True)
  print("Photos uploaded to: "+new_path)
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
