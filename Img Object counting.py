# problem = count the number of objects of a certain type in an image 
# solved = by contour detection and image segmentation

# import library
import cv2
import numpy

# read image and resize image 
img = cv2.imread("img_path")
img_resize = cv2.resize(img,None,fx=0.9,fy=0.9)

# image convert to gray scale 
gray = cv2.cvtColor(img,cv2.COLOR_BG2GRAY)

# image convert to binary scale by thresholding 
ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# image contour 
conture,hierarchy = cv2.findContours(binary,mode=cv2.RETR_TREE,method=cv2.CHAIN_APPROX_NONE)

# visualize contour data
print("length of contour{}".format(len(conture)))
print("contour")

# copy image and draw boundary box 
copy_img = img.copy()
final_img = cv2.drawContours(copy_img,conture,-1,(0,255,0),thickness=2,lineType=cv2.LINE_AA)

#show the final result 
cv2.imshow('obj-counting',final_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
 


