## Script for Raspberry Pi and Pi camera
##    - Camera on / off controlled by trigger input (HI/LO)
##    - Default is rot = 180, 640 x 480, 90 fps... parameters can be modified in picamVideo and picamPreview functions
##    - Default uses GPIO24 as pull_up with Arduino pin and GPIO17 controls indicator LED
## v1.0 7/28/14 by Jason Coleman
## Tried to make button-only loop - Still in progress 9-29-14
## 10-17-14: try to add a preview, dropbox upload step before preceeding with elapse
##           so that it can be used headless via SSH (with AC power and wifi) OR
##           interact with camera GUI

import RPi.GPIO as GPIO
import time, os, picamera, subprocess, sys
from time import gmtime, strftime

image_filenames = "test"
picam_options = "-ev 600 -tl "
time_between_pics = 15 # enter time between pics in seconds
time_overall = 30 # enter overall imaging timespan in seconds

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT) # GPIO17 for LED

time_file = strftime("%Y-%m-%d_%H%M%S") #used to create a unique file name each time
targetDir = "/home/pi/RyanImages/" #"/media/UNTITLED1/movies"
img_filename = targetDir+time_file+".jpg"

##camera = picamera.PiCamera() # WRONG???

def picamPreview(preview_secs):
    with picamera.PiCamera() as camera:
        print("Starting preview...please wait...")
        camera.rotation = 270
        camera.start_preview()
        time.sleep(preview_secs)
        #camera.capture(img_filename)
        camera.stop_preview()
        
def picamVideo():
    while True:
        with picamera.PiCamera() as camera:
            camera.resolution = (640,480)
            camera.framerate = 90
            camera.rotation = 270
            camera.start_recording(target_dir+vid_filename)
            print("Press left button to exit")
            GPIO.wait_for_edge(23,GPIO.FALLING)
            camera.stop_recording()
            stoptime = strftime("%Y-%m-%d %H:%M:%S")
            break;
##            if (GPIO.input(23) == True):
##                break;

def picamTimelapse():
        print("Started timelpse at: "+starttime)
        print("CAMERA TAKING PICS EVERY x secs for y minutes ... ")
        GPIO.output(17,GPIO.HIGH)
        os.system("raspistill "+picam_options+"5000 -rot 180 -t 15000 -o "+targetDir+time_file+"_%04d.jpg")
        GPIO.output(17,GPIO.LOW)
        stoptime = strftime("%Y-%m-%d %H:%M:%S")
        print("CAMERA OFF: Press left button to exit")

##while True:
def queryPreview():
    while True:
        var = raw_input("Ready to begin? (y/n): ")
        if (str(var) == 'y'):
            var_secs = raw_input("Preview time (s): ")
            picamPreview(int(var_secs))
            global var_fileheader 
            var_fileheader = raw_input("Enter movie ID and day: ")
            print("Camera ready...")
            print("Waiting for trigger...")
            break;
        if (str(var) == 'n'):
            var_quit = raw_input("Press Ctrl+C to quit...")

queryPreview()            

while True:
    gpio24_state = GPIO.input(24)
    if(gpio24_state == False): # this would be the trigger input pin (may need to be ==0 depending on trigger input
        GPIO.output(17,GPIO.LOW)
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
        
        picamVideo()

        GPIO.output(17,GPIO.HIGH)

        print("CAMERA OFF")
        stoptime = strftime("%Y-%m-%d %H:%M:%S")
        # print("ENTER new file name: ")
        print(" ")
        print("Stopped recording at: "+stoptime)
        #print("     H264 to mp4 example: $ MP4Box -add "+vid_filename+" newvid.mp4")

        from subprocess import call
        mp4conversion = ("MP4Box -add "+target_dir+vid_filename+" "+target_dir+mp4_filename)
        call ([mp4conversion], shell=True)
        print(vid_filename+" converted to "+mp4_filename)

        break;

        #queryPreview() # note 11/30/14 - re-query does not work!
    
GPIO.cleanup()
