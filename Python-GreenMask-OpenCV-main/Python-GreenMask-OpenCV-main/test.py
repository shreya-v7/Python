import cv2
import numpy as np

img = cv2.imread("image.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# range of color given
mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

# green mask to slice out that part of the image
imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

#displaying in different windows
cv2.imshow("green-masked", green)
cv2.imshow("original", img)
