import urllib
import requests
import cv2
import numpy as np
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Replace the URL with your own IPwebcam shot.jpg IP:port
url = cv2.VideoCapture("http://192.168.43.1:8080/video")


while True:
    check , img = url.read()  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.25, 5)                    #Detect Faces
                                                                            #Rectangle Formation for face 
    for (x,y,w,h) in faces:                                                     
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]       
        eyes = eye_cascade.detectMultiScale(roi_gray)   
        for (ex,ey,ew,eh) in eyes:                                          #Detect Eyes
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)      #Rectangle Formation for eyes
	
	
	
    cv2.imshow('Mob Cam',img)
    if(cv2.waitKey(1)== ord('d')):   #Press 'd' to terminate video 
       break

url.realease()
cv2.destroyAllWindows()

 
