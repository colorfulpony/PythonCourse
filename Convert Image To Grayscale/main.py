import cv2
import os

images = os.listdir('images')
for image in images:
    gray_image = cv2.imread(f'images/{image}', 0)
    cv2.imwrite(f'gray-images/gray-{image}', gray_image)