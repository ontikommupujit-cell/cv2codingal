import cv2

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
smile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

cap=cv2.VideoCapture(0)

print("Press 'q' to quit")

while True:
    ret,frame=cap.read()

    if not ret:
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,5,minSize=(60,60))

    for (x,y,w,h) in faces:

        face_gray=gray[y:y+h,x:x+w]

        smiles=smile_cascade.detectMultiScale(face_gray,1.8,20,minSize=(25,25))

        eyes=eye_cascade.detectMultiScale(face_gray,1.1,5,minSize=(20,20))

        if len(smiles)>0:
            emotion="Happy"
        elif len(eyes)==0:
            emotion="Eyes Closed"
        else:
            emotion="Neutral"

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.putText(frame,emotion,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

    cv2.putText(frame,f"Faces: {len(faces)}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

    cv2.imshow("Real-Time Face & Emotion Detection",frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()