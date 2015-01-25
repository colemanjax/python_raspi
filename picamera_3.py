import time
import picamera

with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.start_preview()
    time.sleep(3)
    camera.capture('foo.jpg')
    camera.stop_preview()

from subprocess import call
photofile = "sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Desktop/foo.jpg /Apps/ColemanPiUploader/"
call ([photofile], shell=True)
