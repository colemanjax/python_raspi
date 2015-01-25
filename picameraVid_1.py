import time, os, picamera

with picamera.PiCamera() as camera:
    camera.rotation = 90
    camera.start_preview()
    time.sleep(10)
    #camera.capture('foo.jpg')
    camera.stop_preview()

filename = "A.h264"
#picam_options = "-p" #"-f"
#picam_options = "-ss 800000 -ex sports -ev 25"
#picam_options = "-ex backlight" -ex night
#picam_options = "-ex night"

os.system("raspivid -rot 90 -fps 90 -w 640 -h 480 -t 5000 -o /home/pi/picam_vids/A.h264")
#os.system("raspistill "+picam_options+" -rot 180 -t 1000 -o /home/pi/picam_imgs/"+filename)
#os.system("raspistill "+picam_options+" -tl 2000 -rot 180 -t 6000 -o /home/pi/pythoncode/foo_%d.jpg")


##from subprocess import call
##photofile = "sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/picam_vids/"+filename+" /Apps/ColemanPiUploader/"
##call ([photofile], shell=True)

##os.system("raspivid -o "+target_dir+vid_filename+" -fps "+fps+" -w 640 -h 480 -rot "+rotation_deg+" -i pause -k")

