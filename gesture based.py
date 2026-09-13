import cv2,mediapipe as mp, numpy as np
from py.caw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
Hand=mp.solutions.hands
hands=Hand.Hands(max_num_hands=0.7,min_detection_confidence=0.7)
draw=mp.solutions.drawing_utils
TH,IX=Hand.HandLandmark.THUMB_TIP,Hand.HandLandmark.INDEX_FINGER_TIP
try:
    dev=AudioUtilities.GetDefaultOutputDevice()if hasattr(AudioUtilities,'GetDefaultOutputDevice')else AudioUtilities.GetSpeakers()
    volctl=dev.EndpointVolume.QueryInterface(IAudioEndpointVolume)
    minv,maxv=volctl.GetVolumeRange()[:2]
except Exception as e:
    print(f'Pycaw error: {e}');exit()
cap.cv2.VideoCapture(0)
if not cap.isOpened():
    print('Webcam could not be opened');exit()
WIN='Hand Gesture Control';cv2.namedWindow(WIN,cv2.WINDOW_NORMAL)
while True:
    ok,img=cap.read()
    if not ok:break
    img=cv2.flip(img,1);h,w=img.shape[:2]
    res=hands.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    if