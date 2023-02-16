import cv2
import os

images = os.listdir('images')

def calculate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)

    return (new_width, new_height)

def resize_image(image_path, slace_percentage, resized_path):
    image = cv2.imread(image_path)
    new_dim = calculate_size(slace_percentage, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)
    cv2.imwrite(resized_path, resized_image)

def resize_images(images, scale_recentage, resized_path):
    for image in images:
        resize_image(f'images/{image}', scale_recentage, f'{resized_path}/resized-{image}')

resize_images(images, 10, 'resized-images')
