# Recognize human emotions from facial expression in webcam

import cv2
from deepface import DeepFace

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fronttalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    result = DeepFace.analyze(frame, actions= ['emotion'])
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray_scale,1.1,4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

        cv2.putText(frame, result['dominant_emotion'], (50,50), cv2.FONT_HERSHEY_SIMPLEX, 3,
                    (0,255,0), 2, cv2.LINE_4)
        cv2.imshow('recognition',frame)

        if cv2.waitKey (10) == ord('q'):
         break

    cap.release()
    cv2.destroyAllWindows()
    