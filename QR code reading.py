import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True :
    ret , frame = cap.read()

    QR_info = decode(frame)

    if len(QR_info)>0:
       QR = QR_info[0]

       data = QR.data
       rect = QR.rect
       polygon = QR.polygon

       cv2.putText(frame, data.decode(), (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

       frame = cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.hight)
                             (0,255,0), 5)
       frame = cv2.polylines(frame, [np.array(polygon)], True, (255,0,0), 5)

    cv2.imshow('QR code',frame)
     
    if cv2.waitKey (10)==ord('q'):
     break

cap.release()
cv2.destroyAllWindows()