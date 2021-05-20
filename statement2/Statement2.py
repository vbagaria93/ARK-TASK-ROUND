from cv2 import cv2 as cv2
import numpy as np
from time import process_time
capture=cv2.VideoCapture('sample.mp4')
t0=process_time()
face_d=cv2.CascadeClassifier('haar_face2.xml')
i=int(input('Enter the starting x coordinate of the particle : '))
j=int(input('Enter the starting y coordinate of the particle : '))
velox=int(input ('Enter velocity in x direction as an integer : '))
veloy=int(input('Enter velocity in y direction as an integer : '))
while True:
     ret,img=capture.read()
     height,width=img.shape[:2]
     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     img_tomask=np.zeros(img.shape[:2],dtype='uint8')
     gray=cv2.flip(gray,1)
     cv2.circle(img_tomask,(i,j),30,(255,123,178),thickness=cv2.FILLED)
     faces=face_d.detectMultiScale(gray,1.3,5,minSize=(30,30))
     for (x,y,w,h) in faces:
         e=cv2.circle(gray[y:y+h,x:x+w],(((w)//2),((h)//2)),(h+w)//4,(0,255,0),thickness=2)
         img_tomask[y:y+h,x:x+w]=e
         cv2.imshow('f',img_tomask)
         if (i < 30) :
           i=30
           velox=-velox
         if (i+30)> width:
           i= width-30
           velox=-velox
         if j < 30 :
           j=30
           veloy=-veloy
         if(j+30)>height :
           x1= float((process_time()-t0)/60)
           print("Time Elapsed in minutes is ",x1)
           quit()
         if i in range (x,x+w+1) and j in range (y,y+h+1):
             if ((i<x+(w/2)) ):
                 i=x
                 velox =-velox
                 break
             else :
                 i=x+w
                 velox =-velox
                 
             if (j<y+(h/2)):
                 j=y#remember the previous one al and optimise it accordingly
                 veloy =-veloy
                 break
             else :
                 j=y+h
                 veloy =-veloy
         i+=velox
         j+=veloy    
     if cv2.waitKey(1) & 0xFF == ord('d'):
         break
capture.release()
cv2.destroyAllWindows
         

