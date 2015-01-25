import time, os, picamera

##with picamera.PiCamera() as camera:
##    camera.rotation = 0
##    camera.start_preview()
##    time.sleep(5)
##    camera.capture('foo2.jpg')
##    camera.stop_preview()

filename ="pi2cam_002.jpg"
picam_options = "-p -e -rot 180" #"-f"
###picam_options = "-ss 800000 -ex sports -ev 25"
###picam_options = "-ex backlight" -ex night
###picam_options = "-ex night"
##
os.system("raspistill "+picam_options+" -t 5000 -o /home/pi/picam_imgs/"+filename)
###os.system("raspistill "+picam_options+" -tl 2000 -rot 180 -t 6000 -o /home/pi/pythoncode/foo_%d.jpg")
##

##from subprocess import call
##photofile = "sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/picam_imgs/"+filename+" /Apps/ColemanPiUploader/"
##call ([photofile], shell=True)
