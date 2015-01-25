# code to take a pic and upload to dropbox
import os, time

fileHeader = "test2_00"
iname=1

#while True:
for num in range(1,2):
    #camera.rotation = 180
    myname=fileHeader+str(iname)+".jpg"
    os.system("raspistill -rot 180 -t 1000 -o /home/pi/"+myname)
    time.sleep(4)
    iname+=1

##from subprocess import call
##photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/img /Apps/ColemanPiUploader/"
##call ([photofile], shell=True)
