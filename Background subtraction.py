# Remove the background from a video feed

import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(0)
Segmentor = SelfiSegmentation()

# if you put image on background
# img_background = cv2.imread('folder\1.jpg')

while True:
    ret , frame = cap.read()

    final_frame = Segmentor.removeBG(frame, (255,0,0), cutThreshold= 0.1)

    # final_frame = Segmentor.removeBG(frame, img_background, cutThreshold= 0.1)

    # if you dont want to write extra line then using cvzone.stackImage()
    # frame_stack = cvzone.stackImages([frame, final_frame], 2, 1) 

    cv2.imshow('original', frame )
    cv2.imshow('background remove', final_frame )

    if cv2.waitKey (10) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
