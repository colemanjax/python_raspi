import os, time

fileHeader = "elapseEve_"
new_path = "/home/pi/pythoncode/"
target_path = " /Apps/ColemanPiUploader"

print("uploading "+new_path+" to Dropbox...")

from subprocess import call
photofile = ("sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload "+new_path+ " "+target_path)
call ([photofile], shell=True)

print("sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload "+new_path+ " "+target_path)

print("all fin")
