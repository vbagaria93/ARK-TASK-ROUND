from cv2 import cv2 as cv2
import numpy as np
from time import process_time
#def rescale(frame,scale):
#   width=img.shape[1]*scale
#   height=img.shape[0]*scale
#   dimensions=(height,width)
#   return cv2.resize(frame,dimensions,interpolation=cv2.INTER_CUBIC)
capture=cv2.VideoCapture('demo1.mp4')
t0=process_time()
m=cv2.imread('gam.png')
i=int(input('Enter the starting x coordinate of the ball: '))
j=int(input('Enter the starting y coordinate of the ball : '))
velox=int(input ('Enter velocity in x direction as an integer : '))
veloy=int(input('Enter velocity in y direction as an integer : '))
face_d=cv2.CascadeClassifier('haar_face2.xml')
while True:
     ret,img=capture.read()
     height,width=img.shape[:2]
     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     img_tomask=np.zeros(img.shape[:2],dtype='uint8')
     gray=cv2.flip(gray,1)#use only when feeding the video from webcam otherwise comment it out
     cv2.circle(img_tomask,(i,j),30,(235,206,135),thickness=cv2.FILLED)
     faces=face_d.detectMultiScale(gray,1.1,6,minSize=(20,20),flags=cv2.FONT_HERSHEY_SIMPLEX)
     for (x,y,w,h) in faces:
         #e=rescale(gray[y:y+h,x:x+w],.5)
         img_tomask[y:y+h,x:x+w]=gray[y:y+h,x:x+w]
         cv2.imshow('game_env',img_tomask)
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
           print("Game Over, Time Elapsed in minutes is ",x1)
           quit()
         if i in range (x-5,x+w+10) and j in range (y-5,y+h+10):
             if ((i<x+(w/2)) ):
                 i=x
                 velox =-velox
             elif (i>x+(w/2)):
                 i=x+w
                 velox =-velox
             elif (j<y+(h/2)):
                 j=y#remember the previous one al and optimise it accordingly
                 veloy =-veloy
             else :
                 j=y+h
                 veloy =-veloy
         i+=velox
         j+=veloy    
     if cv2.waitKey(1) & 0xFF == ord('d'):
         break
capture.release()
cv2.destroyAllWindows