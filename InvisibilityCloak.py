import cv2
import time
import numpy as np

#to save the output in a file
#file name will be output.avi
cv2.VideoWriter_fourcc(*"XVID")
#20 is for fpsww
output_file=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
#starting the webcam
cap=cv2.VideoCapture(0)
#allowing the webcam to start by making the code sleep for two seconds
time.sleep(2)
bg=0
#capture the background for 60 frames

for i in range(60):
    ret,bg=cap.read()

#flipping the background
bg=np.flip(bg,axis=1)
#reading the captured frame until the camera is open

while (cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    #flipping the image for consistancy
    img=np.flip(img,axis=1)
    #convert color from BGR to HSV
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #genertaing mask to detect red color
    lower_red=np.array([0,120,50])
    upper_red=np.array([10,255,255])
    mask_1=cv2.inRange(hsv, lower_red, upper_red)
    lower_red=np.array([170,120,70])
    upper_red=np.array([180,255,255])
    mask_2=cv2.inRange(hsv, lower_red,upper_red)

    mask_1=mask_1+mask_2
    #open and expand the image where there is mask 1
    mask_1=cv2.morphologyEx(src, op, kernel)
    