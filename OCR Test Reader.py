# 1. download Tesseract , 2. pip install tesseract & pillow , 

import pytesseract 
from PIL import Image

img = Image.open('file/New folder/read.jpg')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(img))