import time, os, picamera

##with picamera.PiCamera() as camera:
##    camera.rotation = 180
##    camera.start_preview()
##    time.sleep(3)
##    camera.capture('foo.jpg')
##    camera.stop_preview()

filename = "moores"
new_path = "/home/pi/picam_tests/test3/"+time.strftime("%d%m%_H%_M%_S")+"/"
picam_options = "-f"
#picam_options = "-ss 800000 -ex sports -ev 25"
#picam_options = "-ex backlight" -ex night
#picam_options = "-ex night"

os.makedirs(new_path)

os.system("raspistill "+picam_options+" -tl 2000 -rot 180 -t 10000 -o "+new_path+filename+"_%d.jpg")
#os.system("raspistill "+picam_options+" -tl 2000 -rot 180 -t 6000 -o /home/pi/pythoncode/foo_%d.jpg")


##from subprocess import call
##photofile = "sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh -s upload "+new_path+" /Apps/ColemanPiUploader/"
##call ([photofile], shell=True)
##
##print("Photos uploaded to: "+new_path)
