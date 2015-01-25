import os, time

fileHeader = "elapseMoores_"
new_path = "/home/pi/picam_imgs/070614/"
#picam_options = "-mm backlit -ex backlight"
#picam_options = "-ss 800000 -ex sports -ev 25"
picam_options = "-ex backlight"
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
for num in range(1,4):
    for num in range(1,50):
    	myname=fileHeader+str(iname)+".jpg"
    	os.system("raspistill "+picam_options+" -rot 180 -t 1000 -o "+new_path+myname)
    	time.sleep(15)
    	iname+=1
    
    print("uploading image# 0-"+str(iname))
    from subprocess import call
    photofile = ("sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + new_path + " /Apps/ColemanPiUploader/")
    call ([photofile], shell=True)
    print("finsished a stage")

print("all fin")
