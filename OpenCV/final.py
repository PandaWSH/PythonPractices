import numpy as np
import cv2
import math
import serial
import time

#initial parameters
distance = 0.0
font = cv2.FONT_HERSHEY_SIMPLEX
#face cascade import
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
#capture video
cap = cv2.VideoCapture(0)
#cap.set(3,640)
#cap.set(4,480)
arduino = serial.Serial("/dev/ttyACM0", 115200)
flag =0

while (True):
    #capture a single frame
    ret, img = cap.read() #img as huge_frame in the tutorial
    frame = cv2.resize(img,(0,0),fx=1, fy=1, interpolation = cv2.INTER_NEAREST) 
    
    #img = cv2.flip(img, -1) #flip
    
    #create the gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        #just do face detection
        #gray,
        #scaleFactor = 1.3,
        #minNeighbors = 3,
        #minSize = (15,15)
        #)
     
    for (x,y,w,h) in faces:
        distance_i = ((2*3.14*180)/(w+h*360)*1000+3)/2.9
        #print(distance_i) #distance = distance_i * 2.54 (convert inches to cm)
        
        distance = math.floor(distance_i*2.54)
        # Create rectangle around faces
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
        #print(x)
  #      if x:
 #           print('found a face! At distance: ', distance, 'cm','x position is: ',x)
#            x
    
    if (distance >= 20):
        command = str(125)       # query servo position
        angle = str(75) 
        add = command+":"+angle+"\n"
        arduino.write(str.encode(add))
    else:
        command = str(0)       # query servo position
        angle = str(75)
        add = command+":"+angle+"\n"
        arduino.write(str.encode(add))
        #    flag = 1
      
        
    #display the resulting frame
    cv2.putText(frame,'Distance = ' + str(distance) + 'cm', (5,20),font,1,(255,255,255),2)        
    cv2.imshow('FaceDetection',frame)
    cv2.imshow('gray',gray)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: #press 'ESC' to exit
        break
      
    
    
    
cap.release()
cv2.destroyAllWindows()




