## Script for Raspberry Pi and Pi camera
##    - Camera on / off controlled by trigger input (HI/LO)
##    - Default is rot = 180, 640 x 480, 90 fps... parameters can be modified in picamVideo and picamPreview functions
##    - Default uses GPIO24 as pull_up with Arduino pin and GPIO17 controls indicator LED
## v1.0 7/28/14 by Jason Coleman

import RPi.GPIO as GPIO
import time, os, picamera, subprocess, sys
from time import gmtime, strftime

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # GPIO24 for trigger input
GPIO.setup(17, GPIO.OUT) # GPIO17 for LED

##camera = picamera.PiCamera() # WRONG???

def picamPreview(preview_secs):
    with picamera.PiCamera() as camera:
        print("Starting preview...please wait...")
        camera.rotation = 180
        camera.start_preview()
        time.sleep(preview_secs)
        #camera.capture(img_filename)
        camera.stop_preview()
        
def picamVideo():
    with picamera.PiCamera() as camera:
        camera.resolution = (640,480)
        camera.framerate = 90
        camera.rotation = 180
        camera.start_recording(target_dir+vid_filename)
        GPIO.wait_for_edge(24, GPIO.FALLING) # May need to change to GPIO.rising depending on input trigger
        camera.stop_recording()

##while True:
def queryPreview():
    while True:
        var = raw_input("Ready to begin? (y/n): ")
        if (str(var) == 'y'):
            var_secs = raw_input("Preview time (s): ")
            picamPreview(int(var_secs))
            global var_fileheader 
            var_fileheader = raw_input("Enter animal ID and day (e.g.: mouseB_day1): ")
            print("Camera ready...")
            print("Waiting for trigger...")
            break;
        if (str(var) == 'n'):
            var_quit = raw_input("Press Ctrl+C to quit...")

queryPreview()            

while True:
    if(GPIO.input(24) ==1): # this would be the trigger input pin (may need to be ==0 depending on trigger input
        time_file = strftime("%Y%m%d_%H%M%S") #used to create a unique file name each time
        target_dir = "/home/pi/picam_vids/"
        img_filename = "pic_"+var_fileheader+time_file+".jpg"
        vid_filename = "vid_"+var_fileheader+time_file+".h264"
        mp4_filename = "vid_"+var_fileheader+time_file+".mp4"
        starttime = strftime("%Y-%m-%d %H:%M:%S")
        iname=0
        print("Started recording at: "+starttime)
        print("     New filename: "+vid_filename)
        print("     Saved to    : "+target_dir)
        print("CAMERA RECORDING ... ")
        GPIO.output(17,GPIO.HIGH) # LED
        
        picamVideo()
        
        print("CAMERA OFF")
        stoptime = strftime("%Y-%m-%d %H:%M:%S")
        # print("ENTER new file name: ")
        GPIO.output(17,GPIO.LOW) # LED
        print(" ")
        print("Stopped recording at: "+stoptime)
        #print("     H264 to mp4 example: $ MP4Box -add "+vid_filename+" newvid.mp4")

        from subprocess import call
        mp4conversion = ("MP4Box -add "+target_dir+vid_filename+" "+target_dir+mp4_filename)
        call ([mp4conversion], shell=True)
        print(vid_filename+" converted to "+mp4_filename)

        queryPreview()
    
GPIO.cleanup()
