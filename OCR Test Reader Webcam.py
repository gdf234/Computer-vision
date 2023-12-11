# 1. download Tesseract , 2. pip install tesseract & pillow

import cv2
from PIL import Image
from pytesseract import pytesseract

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('80.jpg',frame)
    if cv2.waitKey (5)& 0xFF == ord('q'):
        cv2.imwrite('text read.jpg',frame)
        break
    
    cap.release()
    cv2.destroyAllWindows()

    def tesseract ():
        tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.1'
        img_path = '80.jpg'
        pytesseract.tesseract_cmd = tesseract_path
        text = pytesseract.image_to_string(Image.open(img_path))
        print(text[:-1])
    tesseract()