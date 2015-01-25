import os, time

fileHeader = "elapseInsideLoop_"
new_path = "/home/pi/picam_imgs/041014_elapse_night/"
#picam_options = "-mm backlit -ex backlight"
picam_options = "-ss 800000 -ex sports -ev 25"
#picam_options = "-ex backlight" 
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
for num in range(1,5):
    myname_base=str(iname_base)
    for num in range(1,51):
        myname=fileHeader+str(iname)+"_"+myname_base+".jpg"
        os.system("raspistill "+picam_options+" -rot 180 -t 1000 -o "+new_path+myname)
        time.sleep(30)
        iname+=1
    
    print("uploading image# 0-"+str(iname))
    from subprocess import call
    photofile = ("sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload" + new_path + " /Apps/ColemanPiUploader/")
    call ([photofile], shell=True)
    print("finsished a stage")

    iname_base+=1

print("all fin")
