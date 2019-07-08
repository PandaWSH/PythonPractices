import numpy as np
import cv2
from matplotlib import pyplot as plt

# edge finding
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    edges = cv2.Canny(gray,100,200)


    cv2.imshow('video',edges)
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: #press 'ESC' to exit
        break
    
cap.release()
cv2.destroyAllWindows()