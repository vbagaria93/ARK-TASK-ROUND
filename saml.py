from cv2 import cv2 as cv2
import numpy as np
def rescaleframe(frame):
      dimensions=(2000,1200)
      return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
capture=cv2.VideoCapture('video.mp4')
capture1=cv2.VideoCapture(0)
i=int(input('Enter the starting x coordinate of the particle : '))
j=int(input('Enter the starting y coordinate of the particle : '))
velox= int(input ('Enter velocity in x direction as an integer : '))
veloy= int(input('Enter velocity in y direction as an integer : '))
while True:
   ret, frame=capture.read()
   ret_,xyg=capture1.read()
   xyg=cv2.cvtColor(xyg,cv2.COLOR_BGR2GRAY)
   xyg=cv2.flip(xyg,1)
   xyg=rescaleframe(xyg)
   frame1=xyg
   frame=rescaleframe(frame)
   haar_cascade=cv2.CascadeClassifier('haar_face2.xml')
   faces_rect=haar_cascade.detectMultiScale(xyg,1.1,3)
   for(q,k,w,h) in faces_rect:
       radius=[((q+2*w)//2),(((k+h)//2))]
       kl=(int((w+h)/4))
       cv2.circle(xyg,radius,((w+h)//4)+10,(0,255,0),2)
       mask=cv2.circle(xyg,radius,kl,(0,255,0),2)
       masked=cv2.bitwise_and(frame,frame,mask=mask)
       frame1=cv2.add(masked,frame)
       cv2.circle(frame,(i,j),30,(0,255,0),thickness=cv2.FILLED)
       y=frame1.shape[0]
       x=frame1.shape[1]
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
          break
       i+=velox
       j+=veloy
       break
   cv2.imshow('FRAME',frame1)
   if cv2.waitKey(1) & 0xFF ==ord('d'):
      break
capture.release()
capture1.release()
cv2.destroyAllWindows
   