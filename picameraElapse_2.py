import os, time

fileHeader = "elapseMoores_"
new_path = "/home/pi/picam_imgs/070614_sunset/"
time_total_sec = 180*1000
#picam_options = "-mm backlit -ex backlight"
#picam_options = "-ss 800000 -ex sports -ev 25"
picam_options = "-ev 600" 
#picam_options = "-ex night"
iname_base=1
iname=0

try:
    os.mkdir(new_path)
except OSError:
    if os.path.exists(new_path):
        print("Directory already exists. Continue?")
        try:
            input("Press ENTER to continue or CTRL+C to interrupt.")
        except SyntaxError:
            pass


print("Initiating PiPhotoBooth...")

#while True:
os.system("raspistill "+picam_options+" -tl 15000 -rot 180 -t 1800000 -o "+new_path+"elapseEve_%04d.jpg")

from subprocess import call
photofile = ("sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload "+new_path+" /Apps/ColemanPiUploader/")
call ([photofile], shell=True)

print("all fin")
