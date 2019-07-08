import numpy as np
import cv2
from matplotlib import pyplot as plt

 
frame = cv2.VideoCapture(0)
frame.set(3,640)
frame.set(4,480)

while (True):
    ret, img = frame.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    edges = cv2.Canny(gray,100,200)
    im2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    #if contour_sizes != []:
    try:
        biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        #cv2.drawContours(frame, biggest_contour, -1, (0,255,0), 3)
        #else:
        #cv2.drawContours(frame, contours, -1, (0,255,0), 3)

        x,y,w,h = cv2.boundingRect(biggest_contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.drawContours(frame, contours, -1, (0,255,255), 3)
    except:
        cv2.drawContours(frame, contours, -1, (0,255,255), 3)

    curve2 = bezier.Curve.from_nodes(contour_sizes)
    # Show final output image
    cv2.imshow('colorTest', frame)
    

    #cv2.imshow('video',edges)
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: #press 'ESC' to exit
        break
    
cap.release()
cv2.destroyAllWindows()


#npy format file