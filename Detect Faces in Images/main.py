import cv2
import os

images = os.listdir('images')

for image in images:
    img = cv2.imread(f'images/{image}', 1)
    face_cascade = cv2.CascadeClassifier('faces.xml')

    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    if len(faces) != 0:
        cv2.imwrite(f'images_with_face/{image}', img)
    else:
        print("no faces")