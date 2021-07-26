from cv2 import cv2 as cv2
import numpy as np
import os 
import time
def rescaleframe(frame1,):
   w=400
   q=500
   dimensions=(w,q)
   return cv2.resize(frame1,dimensions,interpolation=cv2.INTER_AREA)
x2=time.time()
capture=cv2.VideoCapture('video.mp4')
capture1=cv2.VideoCapture(0)
i=int(input('Enter the starting x coordinate of the particle : '))
j=int(input('Enter the starting y coordinate of the particle : '))
velox=int(input ('Enter velocity in x direction as an integer : '))
veloy=int(input('Enter velocity in y direction as an integer : '))
while True:
   ret, frame=capture.read()
   ret_,xyg=capture1.read()
   xyg=cv2.cvtColor(xyg,cv2.COLOR_BGR2GRAY)
   xyg=cv2.flip(xyg,1)
   xyg = rescaleframe(xyg)
   frame=rescaleframe(frame)
   haar_cascade=cv2.CascadeClassifier('haar_face2.xml')
   faces_rect=haar_cascade.detectMultiScale(xyg,1.1,4,flags=cv2.CASCADE_SCALE_IMAGE)
   radius=[0,0]
   kl=0
   mask=np.zeros(xyg.shape[:2],dtype="uint8")
   for(q,k,w,h) in faces_rect:
       radius=[((q+2*w+150)//2),(((k+h)//2)+65)]
       kl=(int((w+h)/4))+10
       cv2.circle(xyg,radius,((w+h)//4)+10,(0,255,0),2) 
       masked=cv2.bitwise_and(xyg,xyg,mask=mask) 
       cv2.imshow("ma",masked) 
   mask=cv2.circle(frame,radius,kl,(0,255,0),2)
   frame=cv2.bitwise_and(frame,frame,mask=mask)
   y=frame.shape[0]
   x=frame.shape[1]
   cv2.imshow('pp',xyg)
   cv2.circle(frame,(i,j),30,(0,255,0),thickness=cv2.FILLED)
   if i < 30 :
     i=30
     velox=-velox
   if (i+30)> x:
     i= x-30
     velox=-velox
   if j < 30 :
     j=30
     veloy=-veloy
   if (j+30)>y :
     x1=time.time()
     break
   i+=velox
   j+=veloy
   cv2.imshow('FRAME',frame)
   if cv2.waitKey(20) & 0xFF ==ord('d'):
      break
print("The time taken to terminate  : " , (int(x1-x2)))
capture.release()
capture1.release()
cv2.destroyAllWindows
   
   
