import numpy as np
from cv2 import cv2 as cv2
import sys
sys.setrecursionlimit(10**8)
img=cv2.cvtColor(cv2.imread('images.png'),cv2.COLOR_BGR2GRAY)
img1=cv2.imread('images.png')
c=img1
bnw=img
#The sequence of operations is up(1),right(2),down(3),left(4),default 0
a=np.zeros(10000,dtype='uint8')
b=np.zeros(10000,dtype='uint8')
a1=0
b1=0
def form(i,j,bnw,c,a,b,a1,b1):
     if(a1<=0):
         a1=0
     if (b1<=0):
         b1=0
     if (i in range (85,105) )& (j in range (85,105)):
         return 1
     if(bnw[i-1][j]==0) &(i>=0):
         bnw[i-1][j]=255
         c[i-1][j]=[0,255,255]
         a[a1]=i-1
         b[b1]=j
         return form(i-1,j,bnw,c,a,b,a1+1,b1+1)
     elif(bnw[i][j+1]==0) & (j+1<197):
         bnw[i][j+1]=255
         c[i][j+1]=[0,255,255]
         a[a1]=i
         b[b1]=j+1
         return form(i,j+1,bnw,c,a,b,a1+1,b1+1)
     elif(bnw[i+1][j]==0) & (i+1<197):
         bnw[i+1][j]=255
         c[i+1][j]=[0,255,255]
         a[a1]=i+1
         b[b1]=j
         return form(i+1,j,bnw,c,a,b,a1+1,b1+1)
     elif(bnw[i][j-1]==0) & (j>=0):
         bnw[i][j-1]=255
         c[i][j-1]=[0,255,255]
         a[a1]=i
         b[b1]=j-1
         return form(i,j-1,bnw,c,a,b,a1+1,b1+1)
     else :
         bnw[i][j]=125
         c[i][j]=[125,45,45]
         a[a1]=0
         b[a1]=0
         return form(a[a1],b[b1],bnw,c,a,b,a1-1,b1-1)
j=form(195,2,bnw,c,a,b,a1,b1)
cv2.imshow("c",c)
cv2.waitKey(0)