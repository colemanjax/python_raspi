import RPi.GPIO as GPIO
import time, os, picamera
from time import gmtime, strftime

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT) # GPIO17 for LED

xsec=1
time_file = strftime("%Y-%m-%d_%H%M%S") #used to create a unique file name each time
targetDir = "/media/UNTITLED1/movies"
img_filename = targetDir+"/vid_pic_"+time_file+".jpg"
vid_filename = targetDir+"/vid_"+time_file+".h264"
mp4_filename = targetDir+"/vid_"+time_file+".mp4"

starttime = strftime("%Y-%m-%d %H:%M:%S")
iname=0

print("Starting preview...please wait...")
with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.start_preview()
    time.sleep(5)
    camera.capture(img_filename)
    camera.stop_preview()
print("Camera ready...")

while True:
    #var = raw_input("RECORD NEW VID?: ")
    #if (int(var) == 1):
    if(GPIO.input(24) ==0): # this would be the trigger input pin
        print("Started recording at: "+starttime)
        print("CAMERA RECORDING ... ")
        GPIO.output(17,GPIO.HIGH)
        #os.system("raspivid -w 640 -h480 -fps 90 -t "+str(xsec)+" -o /home/pi/picam_vids/"+filename)
        with picamera.PiCamera() as camera:
##            camera.start_preview()
            camera.rotation = 180
            camera.start_recording(vid_filename)
            GPIO.wait_for_edge(23, GPIO.FALLING) # time.sleep(xsec) # time for testing or recording duration (s)
            camera.stop_recording()
##            camera.start_preview()
            stoptime = strftime("%Y-%m-%d %H:%M:%S")
            print("CAMERA OFF")
            # print("ENTER new file name: ")
            GPIO.output(17,GPIO.LOW)
            #GPIO.wait_for_edge(24, GPIO.RISING)
            break
        #iname+=1
        #vid_filename = "/home/pi/picam_vids/testvid6"+str(iname)+".h264"

GPIO.output(17,GPIO.LOW)
print(" ")
print("Stopped recording at: "+stoptime)
print("H264 to mp4 example: $ MP4Box -add "+vid_filename+" newvid.mp4")

from subprocess import call
photofile = ("MP4Box -add "+vid_filename+" "+mp4_filename)
call ([photofile], shell=True)
print(vid_filename+" converted to MP4: "+mp4_filename)

GPIO.cleanup()
