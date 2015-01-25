import RPi.GPIO as GPIO
import time, os, picamera
from time import gmtime, strftime

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT) # GPIO17 for LED

xsec=20
img_filename = "/home/pi/picam_vids/test6.jpg"
vid_filename = "/home/pi/picam_vids/testvid6.h264"

starttime = strftime("%Y-%m-%d %H:%M:%S")

print("Starting preview...please wait...")
with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.start_preview()
    time.sleep(5)
    camera.capture(img_filename)
    camera.stop_preview()
print("Camera ready...")

while True:
    if(GPIO.input(24) ==0):
        print("Started recording at: "+starttime)
        print("CAMERA RECORDING ... ")
        GPIO.output(17,GPIO.HIGH)
        #os.system("raspivid -w 640 -h480 -fps 90 -t "+str(xsec)+" -o /home/pi/picam_vids/"+filename)
        with picamera.PiCamera() as camera:
            camera.start_recording(vid_filename)
            #time.sleep(xsec)
            #camera.stop_preview()
            GPIO.wait_for_edge(23, GPIO.FALLING) # time.sleep(xsec) # time for testing or recording duration (s)
            camera.stop_recording()
                #break
    #if(GPIO.input(23) ==1):
        #camera.stop_recording()
            stoptime2 = strftime("%Y-%m-%d %H:%M:%S")
            print("CAMERA OFF")
            # print("ENTER new file name: ")
            GPIO.output(17,GPIO.LOW)
            break
        #time.sleep(2)
    #elif(GPIO.input(24) ==1):
        #GPIO.output(17,GPIO.LOW)

#stoptime = strftime("%Y-%m-%d %H:%M:%S")
#camera.stop_preview()
GPIO.output(17,GPIO.LOW)
print(" ")
print("Stopped recording at: "+stoptime2)
print("H264 to mp4 example: $ MP4Box -add "+vid_filename+" newvid.mp4")

from subprocess import call
photofile = ("MP4Box -add "+vid_filename+" "+vid_filename+".mp4")
call ([photofile], shell=True)
print(vid_filename+" converted to MP4")

GPIO.cleanup()
