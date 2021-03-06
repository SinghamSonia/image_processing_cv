import cv2
import numpy as np

img = cv2.imread('Plaque.jpg', 1)
gray = cv2.imread("Plaque.jpg", 0)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imwrite('harris2.jpg',img)