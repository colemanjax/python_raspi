import os, time

fileHeader = "new_00"
iname=0

print("Initiating PiPhotoBooth...")

#while True:
for num in range(1,40):
    myname=fileHeader+str(iname)+".jpg"
    os.system("raspistill -rot 180 -t 1000 -o /home/pi/picam_imgs/"+myname)
    time.sleep(15)
    iname+=1
    print("uploading image# 00"+str(iname))
    from subprocess import call
    photofile = "sudo /home/pi/Dropbox-Uploader/dropbox_uploader.sh -s upload /home/pi/picam_imgs/ /Apps/ColemanPiUploader/picam_imgs/"
    call ([photofile], shell=True)

print("all fin")
