from cv2 import cv2 as cv2
import numpy as np
import math
from time import process_time
def distance(point1,point2):
  return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
#def rescale(frame,scale):
#   width=img.shape[1]*scale
#   height=img.shape[0]*scale
#   dimensions=(height,width)
#   return cv2.resize(frame,dimensions,interpolation=cv2.INTER_CUBIC)
capture=cv2.VideoCapture(0)
t0=process_time()
m=cv2.imread('gam.png')
face_d=cv2.CascadeClassifier('haar_face2.xml')
i=int(input('Enter the starting x coordinate of the ball: '))
j=int(input('Enter the starting y coordinate of the ball : '))
velox=int(input ('Enter velocity in x direction as an integer : '))
veloy=int(input('Enter velocity in y direction as an integer : '))
while True:
     ret,img=capture.read()
     height,width=img.shape[:2]
     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     img_tomask=np.zeros(img.shape[:2],dtype='uint8')
     gray=cv2.flip(gray,1)
     cv2.circle(img_tomask,(i,j),30,(235,206,135),thickness=cv2.FILLED)
     faces=face_d.detectMultiScale(gray,1.1,6,minSize=(20,20),flags=cv2.FONT_HERSHEY_SIMPLEX)
     for (x,y,w,h) in faces:
         #e=rescale(gray[y:y+h,x:x+w],.5)
         #img_tomask[y:y+h,x:x+w]=gray[y:y+h,x:x+w]
         center=(x+w)//2 , (y+h)//2
         cv2.circle(img_tomask,center,(h+w)//6,(100),cv2.FILLED)
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
         if distance(center,(i,j)) <= ((h+w)//6)+30:
           velox=-velox
           veloy=-veloy
         i+=velox
         j+=veloy    
     if cv2.waitKey(1) & 0xFF == ord('d'):
         break
capture.release()
cv2.destroyAllWindows