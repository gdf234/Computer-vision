# Traffic sign Recognition using webcam
import cv2

cap = cv2.VideoCapture(0)

stop_sign = cv2.CascadeClassifier('image_path')

while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.2, 4)

    for (x, y, w, h) in stop_sign_scaled:
        stop_sign_rectangle = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        stop_sign_text = cv2.putText(stop_sign_rectangle,"stop sign"+str(stop_sign_scaled), (x,y-20), 
                                     cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 5)

    cv2.imshow('traffic sign Recognition', frame)
   
    if cv2.waitKey (10) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
