import numpy as np
from cv2 import cv2 as cv2
import sys
import faulthandler
faulthandler.enable()
sys.setrecursionlimit(10**9)
img=cv2.cvtColor(cv2.imread('MAZE_D.png'),cv2.COLOR_BGR2GRAY)
img1=cv2.imread('MAZE_D.png')
c=img1#9:160,8:445]#coloured array to denote the path
bnw=img#[9:160,8:445]#black and white array for path finding
#The sequence of operations is up(1),right(2),down(3),left(4),default 0
a=np.zeros(12000,dtype='uint8')#stacks to store the traversed values
b=np.zeros(12000,dtype='uint8')
def validity(i,j,a): #checking if the path is valid
        if (a[i][j]==0 & (i in range (0,159)) &( j in range (0,445))):
             return 1
        else :
             return 0
a1=0
b1=0
def form(i,j,bnw,c,a,b,a1,b1):
     if(a1<=0):
         a1=0
     if (b1<=0):
         b1=0
     if (i>=135& j>=404):#it denotes that the puzzle is solved
         return 1
     if(validity((i-1),j,bnw)==1):#traverse up
         bnw[i-1][j]=255
         c[i-1][j]=[0,255,255]
         a[a1]=i-1
         b[b1]=j
         return form(a[a1],b[b1],bnw,c,a,b,a1+1,b1+1)
     elif(validity(i,j+1,bnw)==1):#traverse right
         bnw[i][j+1]=255
         c[i][j+1]=[0,255,255]
         a[a1]=i
         b[b1]=j+1
         return form(a[a1],b[b1],bnw,c,a,b,a1+1,b1+1)
     elif(validity((i+1),j,bnw)==1):#traverse down
         bnw[i+1][j]=255
         c[i+1][j]=[0,255,255]
         a[a1]=i+1
         b[b1]=j
         return form(a[a1],b[b1],bnw,c,a,b,a1+1,b1+1)
     elif(validity((i),j-1,bnw)==1):#traverse left
         bnw[i][j-1]=255
         c[i][j-1]=[0,255,255]
         a[a1]=i
         b[b1]=j-1
         return form(a[a1],b[b1],bnw,c,a,b,a1+1,b1+1)
     else :
         bnw[i][j]=125
         c[i][j]=[125,45,45]
         a[a1]=0
         b[a1]=0
         return form(a[a1-1],b[b1-1],bnw,c,a,b,a1-1,b1-1)
j=form(149,3,bnw,c,a,b,a1,b1)

cv2.imshow("c",c)
cv2.waitKey(0)