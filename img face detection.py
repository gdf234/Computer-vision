import cv2

# Load the Classifier
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# import image
img = cv2.imread('New folder\cricket.jpg')

# Convet color to gray image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply face scale into gary image
faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
print("face detected".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
# Display
cv2.imshow('face detected',img)
cv2.waitKey (10000)
  

