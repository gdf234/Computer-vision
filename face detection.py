import cv2

# Load the Classifier
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open webcam
cap = cv2.VideoCapture(0)

# Identifying Faces in the Video Stream
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

# Display
while True:
 ret,video = cap.read()
 faces = detect_bounding_box(video)
 cv2.imshow('face detected',video)
 if cv2.waitKey (10)==ord('q'):
  break

video.release()
        
