import time
import picamera

camera = picamera.PiCamera()

try:
    camera.rotation = 180
    camera.start_preview()
    camera.start_recording('A.h264') #to view: omxplayer test.h264 (or omxplayer -o hdmi test.h264
    camera.wait_recording(2)
    camera.stop_recording()
    #time.sleep(10)
    camera.stop_preview()
finally:
    camera.close()
    
