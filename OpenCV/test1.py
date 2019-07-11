import cv2
import numpy as np 

vid = cv2.VideoCapture('PLA_210Tex_170Tt_1mmRetract_6mms_Default_Pappas.avi')
ret, frame = vid.read()
r = cv2.selectROI(ret)

while (vid.isOpened()):
	
	#frame = frame[0:1000,0:2500]
	# draw a specific area if detectuib
	# Select ROI
    
     
    # Crop image
    imCrop = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

	imgray = cv2.cvtColor(imCrop, cv2.COLOR_BGR2GRAY)

	# adjust threshold
	ret, thresh = cv2.threshold(imgray, 90, 255, 0)
	#im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

	cv2.imshow('frame', thresh)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.releas()
cv2.destroyAllWindows()
