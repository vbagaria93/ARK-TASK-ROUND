import numpy as np
from cv2 import cv2 as cv2
from PIL import Image
def rescaleframe(frame1):
     dimenstions=(2000,1200)
     return cv2.resize(frame1,dimenstions,interpolation=cv2.INTER_AREA)
captue=cv2.VideoCapture(0)
while True:
    ret,xyg=captue.read()
    #blank=np.zeros(xyg.shape[:2],dtype='uint8')
    xyg=cv2.cvtColor(xyg,cv2.COLOR_BGR2GRAY)
    xyg=cv2.flip(xyg,1)
    xyg=rescaleframe(xyg)
    haar_cascade=cv2.CascadeClassifier('haar_face2.xml')
    faces_rect=haar_cascade.detectMultiScale(xyg,1.1,4)
    for(x,y,w,h) in faces_rect:
        radius=((x+2*w+200)//2),(((y+h)//2)+65)
        cv2.circle(xyg,radius,((w+h)//4),(0,255,0),2)
        #blank=cv2.circle(blank,radius,((w+h)//4)+10,(0,255,0),2)
        #jcole=cv2.bitwise_and(xyg,xyg, mask=blank)
    cv2.imshow('small pp',xyg)
    if(cv2.waitKey(1) & 0xFF==ord('d')):
        break    
captue.release()
cv2.destroyAllWindows()
