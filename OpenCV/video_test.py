import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
 
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 3,
        minSize = (15,15)
        )
    # Create rectangle around faces
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
        #print signal
        if x:
            print('found a face!')
            
    cv2.imshow('video',img)
    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: #press 'ESC' to exit
        break
    
cap.release()
cv2.destroyAllWindows()

'''
prvTime = 3

#for x in range(3):
    #change the resolution
camera.resolution = (640,480)

#run camera preview
#time.sleep(3)

#capture a picture
camera.start_preview()
time.sleep(prvTime)
camera.capture('PiCameTest.jpg')
camera.stop_preview()
camera.close()

# Load a cascade file for detecting faces
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# Load image
image = cv2.imread('PiCameTest.jpg')

# Convert into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

########### test gray conversion (2 lines) #########
#cv2.imshow('gray',gray)
#cv2.waitKey(0)

########### convert to yuv and test (6 lines) ###############
img_to_yuv = cv2.cvtColor(image,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
yuv = cv2.cvtColor(img_to_yuv,cv2.COLOR_YUV2BGR)
#cv2.namedWindow('yuv',cv2.WINDOW_AUTOSIZE)
#cv2.imshow('yuv',yuv)
#cv2.waitKey(0)


# Look for faces in the image using the loaded cascade file
faces = faceCascade.detectMultiScale(yuv, 1.2, 2)
for (x,y,w,h) in faces:
        # Create rectangle around faces
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),2)
        print(x)
        if x:
            print('found a face!')

# Create the resizeable window
cv2.namedWindow('gray', cv2.WINDOW_AUTOSIZE)

# Display the image
cv2.imshow('gray', image)
#cv2.imwrite('AndrewDetected.jpg',image)

# Wait until we get a key
k=cv2.waitKey(0)

# If pressed key is 's'
if k == ord('s'):
     # Save the image
     cv2.imwrite('FaceDetected.jpg', image)
     # Destroy all windows
     cv2.destroyAllWindows()
     # If pressed key is ESC
elif k == 27:
     # Destroy all windows
     cv2.destroyAllWindows()
'''

