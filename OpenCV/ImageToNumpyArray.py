# image to numpy array
import cv2
import numpy as np

img1 = cv2.imread('pic19.jpg')
img2 = cv2.imread('pic31.jpg')
img1 = img1[0:560,480:660] 
img2 = img2[0:560,480:660] 
rett1, thresh1 = cv2.threshold(img1, 100, 255, 0)
rett2, thresh2 = cv2.threshold(img2, 100, 255, 0)

diff = cv2.absdiff(thresh1,thresh2)
mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

th = 1
imask = mask > th

canvas = np.zeros_like(img2, np.uint8)
canvas[imask] = img2[imask]

cv2.imwrite("result.png", canvas)

'''
np.save('data1',thresh)
cv2.imshow('image44',thresh)
k = cv2.waitKey(0)

if cv2.waitKey(1) & 0xFF == ord('q'):
	cv2.destroyAllWindows()

#read the numpy array data
a = np.load('data19.npy')
b = a = np.load('data31.npy')
print(len(a))
'''