## Script for Raspberry Pi and Pi camera
##    - Camera on / off controlled by trigger input (HI/LO)
##    - Camera/Video parameters can be modified in variables listed after imports
##    - Default uses GPIO24 as pull_up with Arduino pin and GPIO17 controls indicator LED
## v1.0 7/28/14 by Jason Coleman
## Tried to make button-only loop - Still in progress 9-29-14
## 10-17-14: try to add a preview, dropbox upload step before preceeding with elapse
##           so that it can be used headless via SSH (with AC power and wifi) OR
##           interact with camera GUI
## 12-3-14: cleaned up code, added parameter variables at code start;

## GPIO pin wiring scheme for 2-button circuit:
##     blue = rt btn_R (24)
##     purple = LED+ (pin4,--) :  does -- = 5V?, then try pin1,3V
##     gray = rt btn_L (pin6,gnd)
##     white = lt btn_R (23)
##     black = lt btn_L and resistor(->LED-) (17)
## Also, reversing black and purple might make GPIO.HIGH = led on again (now its "intuitively" reversed)


import RPi.GPIO as GPIO
import time, os, picamera, subprocess, sys
from time import gmtime, strftime

# Filenames and parameters
targetDir = "/home/pi/RyanImages/" # for time lapse function "/media/UNTITLED1/movies"
target_dir = "/home/pi/picam_vids/" # for video function should move this to top and video filenames to video function?
image_filenames = "test"
picam_options = "-ev 600 -tl "
time_between_pics = 15 # enter time between pics in seconds
time_overall = 30 # enter overall imaging timespan in seconds
rotation_deg = 90
fps = 30 # default = 30
resolution = (1920,1080) # default/full res = 1920,1080
# do not alter code below this line

if (fps == 90):
    resolution = (640,480) # 90fps only works at 640,480

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT) # GPIO17 for LED

time_file = strftime("%Y-%m-%d_%H%M%S") #used to create a unique file name each time
img_filename = targetDir+time_file+".jpg"

def picamPreview(preview_secs):
    with picamera.PiCamera() as camera:
        print("Starting preview...please wait...")
        camera.rotation = rotation_deg
        camera.start_preview()
        time.sleep(preview_secs)
        #camera.capture(img_filename)
        camera.stop_preview()
        
def picamVideo():
    while True:
        with picamera.PiCamera() as camera:
            camera.resolution = resolution
            camera.framerate = fps
            camera.rotation = rotation_deg
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
        print("Press left button to exit")

##while True:
def queryPreview():
    while True:
        GPIO.output(17,GPIO.LOW)
        var = raw_input("Ready to begin? (y/n): ")
        if (str(var) == 'y'):
            var_secs = raw_input("Preview time (s): ")
            picamPreview(int(var_secs))
            global var_fileheader 
            var_fileheader = raw_input("Enter unique file ID tag: ")
##            for i in range (1,5):
##                GPIO.output(17,GPIO.HIGH)
##                time.sleep(1)
##                GPIO.output(17,GPIO.LOW)
            GPIO.output(17,GPIO.HIGH)
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
