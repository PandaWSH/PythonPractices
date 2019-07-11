import cv2
import numpy as np 

'''
def rotateImage(image, angle):
    row,col = image.shape
    center=tuple(np.array([row,col])/2)
    rot_mat = cv2.getRotationMatrix2D(center,angle,1.0)
    new_image = cv2.warpAffine(image, rot_mat, (col,row))
    return new_image
'''

vid = cv2.VideoCapture('test7_10_3.avi')
#PLA_210Tex_170Tt_3mmRetract_6mms
#PETG_firstload_3mmoffset,15mmwindow_red [not good for current code]
#PLA_210Tex_170Tt_1mmRetract_4mms_Default
#PLA_210Tex_170Tt_1mmRetract_6mms_Default_Pappas

while (vid.isOpened()):
	ret, frame = vid.read()
	imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#imgray = imgray[0:560,480:660] # draw a specific area if detect
	# adjust threshold
	rett, thresh = cv2.threshold(imgray, 85, 225, 0)
	# contour
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	'''
	for contour in contours:
	   	cv2.drawContours(thresh, contours, -1, (200,200,0), 2)

	# find the biggest contour
	contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
	biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
	cv2.drawContours(thresh, [biggest_contour], -1, (200,200,0), 3)
	
	# same video to image
	def getFrame(sec):
	    vid.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
	    ret, frame = vid.read()
	    if ret:
	        cv2.imwrite("pic"+str(count)+".jpg", thresh)     # save frame as JPG file
	    return ret
	sec = 0
	frameRate = 2 #//it will capture image in each 2 second
	count=1
	success = getFrame(sec)
	while success:
	    count = count + 1
	    sec = sec + frameRate
	    sec = round(sec, 2)
	    success = getFrame(sec)
	'''

	cv2.rectangle(thresh,(600,0),(370,900),(200,200,0),3)
	cv2.imshow('frame', thresh)
	#cv2.nameWindow('frame',WINDOW_NORMAL)
	#cv2.resize(thresh,(480,720))
	cv2.imshow('grayscale',imgray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cv2.destroyAllWindows()
