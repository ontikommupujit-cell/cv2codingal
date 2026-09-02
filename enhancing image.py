import cv2
import numpy as np

cap=cv2.VideoCapture(0)
mode="normal"

while True:
    ret,frame=cap.read()

    if mode=="red":
        frame[:,:,0]=0
        frame[:,:,1]=0

    elif mode=="green":
        frame[:,:,0]=0
        frame[:,:,2]=0

    elif mode=="blue":
        frame[:,:,1]=0
        frame[:,:,2]=0

    elif mode=="sobel":
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame=cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=3)

    elif mode=="canny":
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame=cv2.Canny(gray,100,200)

    cv2.imshow("Camera",frame)

    key=cv2.waitKey(1)&0xFF

    if key==ord("r"):
        mode="red"
    elif key==ord("g"):
        mode="green"
    elif key==ord("b"):
        mode="blue"
    elif key==ord("s"):
        mode="sobel"
    elif key==ord("c"):
        mode="canny"
    elif key==ord("q"):
        break
    elif key!=255:
        print("Invalid key")

cap.release()
cv2.destroyAllWindows()