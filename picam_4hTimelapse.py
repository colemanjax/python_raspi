import os, time
from time import gmtime, strftime
import picamera


fileHeader = "elapseMoores_"
time_file = strftime("%Y%m%d_%H%M%S")
new_path = "/home/pi/picam_imgs/"+time_file+"/"
time_total_sec = 20000#14400*1000
#picam_options = "-mm backlit -ex backlight"
#picam_options = "-ss 800000 -ex sports -ev 25"
picam_options = "-n" # disables preview window 
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


os.system("raspistill "+picam_options+" -tl 15000 -t 14400000 -o "+new_path+"timelapse_%04d.jpg")
##
##from subprocess import call
##photofile = ("sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload "+new_path+" /Apps/ColemanPiUploader/")
##call ([photofile], shell=True)
##
##print("all fin")
