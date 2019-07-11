## Read and convert 
import cv2
import numpy as np
from skimage import io
img = io.imread('pic31.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

## Find outer contours 
_, cnts, _= cv2.findContours(gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

## Draw 
canvas = np.zeros_like(img)
cv2.drawContours(canvas , contours, -1, (0, 255, 0), 1)

plt.imshow(canvas)