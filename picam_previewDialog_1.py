import RPi.GPIO as GPIO
import time, os, picamera, subprocess
from time import gmtime, strftime

def picamPreview(preview_secs):
    print("Starting preview...please wait...")
    with picamera.PiCamera() as camera:
        camera.rotation = 180
        camera.start_preview()
        time.sleep(preview_secs)
        #camera.capture(img_filename)
        camera.stop_preview()

picamPreview(5)

while True:        
    var = raw_input("Ready to begin? (y/n): ")
    if (str(var) == 'y'):
        print("Camera ready...")
        break;
    if (str(var) == 'n'):
        #run the preview function
        var_secs = raw_input("Preview time (s): ")
        picamPreview(int(var_secs))

print("out")
