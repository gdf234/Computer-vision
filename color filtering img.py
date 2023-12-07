import cv2
import numpy as np

img = cv2.imread('New folder\satellite.jpg')

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh = 80
maxval = 255
ret , thresh = cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold', thresh)
cv2.waitKey(50000)
    
