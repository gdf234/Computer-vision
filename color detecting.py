import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
  ret , frame = cap.read()
  BGR_HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

  # for red color   
  lower_red = np.array([161,155,84])
  upper_red = np.array([179,255,255])
  red_mask = cv2.inRange(BGR_HSV,lower_red,upper_red)
  red = cv2.bitwise_and(frame,frame,mask=red_mask)

  # for blur color 
  lower_blue = np.array([161,155,84])
  upper_blue = np.array([179,255,255])
  blue_mask = cv2.inRange(BGR_HSV,lower_blue,upper_blue)
  blue = cv2.bitwise_and(frame,frame,mask=blue_mask)

  # for green color 
  lower_green = np.array([25,52,72])
  upper_green = np.array([102,255,255])
  green_mask = cv2.inRange(BGR_HSV,lower_green,upper_green)
  green = cv2.bitwise_and(frame,frame,mask=green_mask)


  cv2.imshow('original',frame)
  cv2.imshow('green',green)
  if cv2.waitKey(2) == ord('q'):
        break


                
