import RPi.GPIO as GPIO
import time, os, picamera
from time import gmtime, strftime

image_filenames = "test"
picam_options = "-ev 600 -tl "
time_between_pics = 5 # enter time between pics in seconds
time_overall = 30 # enter overall imaging timespan in seconds
preview_time = 10 # enter time for preview in seconds

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT) # GPIO17 for LED

time1 = (time_between_pics*1000)
time2 = (time_overall*1000)
time_file = strftime("%Y-%m-%d_%H%M%S") #used to create a unique file name each time
targetDir = "/home/pi/RyanImages/" #"/media/UNTITLED1/movies"
img_filename = targetDir+time_file+".jpg"
vid_filename = targetDir+"/vid_"+time_file+".h264"
mp4_filename = targetDir+"/vid_"+time_file+".mp4"

starttime = strftime("%Y-%m-%d %H:%M:%S")
iname=0

print("Starting preview...please wait...")
with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.start_preview()
    time.sleep(preview_time)
    #camera.capture(img_filename)
    camera.stop_preview()
print("Camera ready...")

while True:
    if (GPIO.input(24) == 0): # this would be the trigger input pin
        print("Started recording at: "+starttime)
        print("CAMERA RECORDING ... ")
        GPIO.output(17,GPIO.HIGH)
        os.system("raspistill "+picam_options+str(time1)+" -rot 180 -t "+str(time2)+" -o "+targetDir+time_file+"_%04d.jpg")
        GPIO.output(17,GPIO.LOW)
        stoptime = strftime("%Y-%m-%d %H:%M:%S")
        print("CAMERA OFF: Press left button to exit")

        GPIO.wait_for_edge(23, GPIO.FALLING)# time.sleep(xsec) # time for testing or recording duration (s)
        GPIO.output(17,GPIO.LOW)
        break

GPIO.output(17,GPIO.LOW)
print(" ")
stoptime = strftime("%Y-%m-%d %H:%M:%S")
print("Stopped recording at: "+stoptime)
##print("H264 to mp4 example: $ MP4Box -add "+vid_filename+" newvid.mp4")
##
##from subprocess import call
##photofile = ("MP4Box -add "+vid_filename+" "+mp4_filename)
##call ([photofile], shell=True)
##print(vid_filename+" converted to MP4: "+mp4_filename)

GPIO.cleanup()
