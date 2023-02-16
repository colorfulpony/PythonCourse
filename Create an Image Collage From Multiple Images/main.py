import cv2
import os
import numpy

columns = 3
rows = 2

horizontal_margin = 40
vertical_margin = 40

images = os.listdir('images')
image_object = [cv2.imread(f'images/{filename}') for filename in images]

shape = cv2.imread('images/1.jpeg').shape

big_image = numpy.zeros((shape[0] * rows + (rows + 1) * horizontal_margin,
                        shape[1] * columns + (columns + 1) * vertical_margin,
                        shape[2]),
                        numpy.uint8
                        )

big_image.fill(255)

positions = [(x, y) for x in range(columns) for y in range(rows)]

for (pos_x, pos_y), image in zip(positions, image_object):
    x = pos_x * (shape[1] + vertical_margin) + vertical_margin
    y = pos_y * (shape[0] + horizontal_margin) + horizontal_margin
    big_image[y:y+shape[0], x:x+shape[1]] = image

cv2.imwrite('grid.jpeg', big_image)