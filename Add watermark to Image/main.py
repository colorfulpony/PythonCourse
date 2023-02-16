import cv2

image = cv2.imread('air.jpg')
watermark = cv2.imread('img.png')

print(image.shape)
print(watermark.shape)

x = image.shape[1] - watermark.shape[1]
y = image.shape[0] - watermark.shape[0]

watermark_place = image[y:, x:]
cv2.imwrite('watermark_place.jpeg', watermark_place)

blend = cv2.addWeighted(watermark_place, 0.5, watermark, 0.5, 0)
cv2.imwrite('blend.jpg', blend)

image[y:, x:] = blend
cv2.imwrite('img_with_watermark.jpg', image)