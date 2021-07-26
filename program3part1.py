from cv2 import cv2 as cv2
import numpy as np
from PIL import Image
img=cv2.cvtColor(cv2.imread('Level1.png'),cv2.COLOR_BGR2RGB)
img1=cv2.cvtColor(cv2.imread('zucky_elon.png'),cv2.COLOR_BGR2RGB)
a=(np.array(img)).tolist()
b=np.array(img)
t=0
for i in range (0,6):
   for j in range (0,177):
          a[i][j][0]=chr(a[i][j][0])
          print(a[i][j][0],end="")
for z in range (0 ,94):
        a[6][z][0]=chr(a[6][z][0])
        print(a[6][z][0],end="")
#for j in range (0,5):
     #for k in range (0,3):
        # print (a[176][j][k] ,end="")
c=np.zeros((200,150,3),dtype='uint8')
for j in range (0,83):
       for k in range (0,3):
           c[0][j][k]=b[6][94+j][k]
for j in range (83,150):
        for k in range (0,3):
            c[0][j][k]=b[7][t][k]
        t+=1
for j in range (0,110):
        for k in range (0,3):
            c[1][j][k]=b[7][t][k]
        t+=1
t=110
q=1
for i in range (8,176):
    for j in range (0,177):
            if t==150:
                t=0
                q+=1
            for k in range (0,3):
                c[q][t][k]=b[i][j][k]
            t+=1
print(t)
h=Image.fromarray(c)
h.show()
h.save('atbash12.png')
pq=cv2.cvtColor(cv2.imread('atbash12.png'),cv2.COLOR_BGR2RGB)
h1=cv2.matchTemplate(img1,pq,cv2.TM_SQDIFF_NORMED)
cv2.imshow('h1',h1)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(h1)
print(min_loc[0])
