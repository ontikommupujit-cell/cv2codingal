import cv2,time,pyautogui
import mediapipe as mp
mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7)
mp_draw=mp.solutions.drawing_utils
SCROLL_SPEED=300
SCROLL_DELAY=1
CAM_WIDTH, CAM_HEIGHT=640,480
def detect_gesture(landmarks, handedness):
    fingers=[]
    tips=[mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
    for tip in tips:
        if landmarks.landmark[tip].y<landmarks.landmark[tip-2].y:
            fingers.append(1)
    thumb_tip=landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip=landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    if (handedness=='Right' and thumb_tip.x>thumb_ip.x)or (handedness=='Left' and thumb_tip.x<thumb_ip.x):
        fingers.append(1)
        return 'Scroll Up' if sum(fingers)==5 else 'Scroll Down'if len(fingers)==0 else 'No Gesture'
cap=cv2.VideoCapture(0)
cap.set(3,CAM_WIDTH)
cap.set(4,CAM_HEIGHT)
last_scroll_time=p_time=0
print('gesture based scrolling started')
while cap.isOpened():
    success,img=cap.read()
    if not success:break
    img=cv2.flip(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),1)
    results=hands.process(img)
    gesture, handedness='No Gesture','Unknown'
    if results.multi_hand_landmarks:
        for hand,handedness_info in zip(results.multi_hand_landmarks,results.multi_handedness):
            handedness=handedness_info.classification[0].label
            gesture=detect_gesture(hand, handedness)
            if time.time()-last_scroll_time>SCROLL_DELAY:
                if gesture=='Scroll Up':
                    pyautogui.scroll(SCROLL_SPEED)
                    last_scroll_time=time.time()
                elif gesture=='Scroll Down':
                    pyautogui.scroll(-SCROLL_SPEED)
                    last_scroll_time=time.time()
        fps=1/(time.time()-p_time) if (time.time()-p_time)>0 else 0
        p_time=time.time()
        cv2.putText(img,f'Gesture: {gesture}',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('Gesture Based Scrolling',cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
        if cv2.waitKey(1)&0xFF==ord('q'):break
cap.release()
cv2.destroyAllWindows()