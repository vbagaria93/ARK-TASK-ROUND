
from cv2 import cv2 as cv2
import sys
sys.setrecursionlimit(10**8)
import numpy as np
im=cv2.imread('MAZE_D.png')
img=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
img[140:155, 3:41] = 0
img[140:155, 400:441] = 0
start = [142,38]
stack=[]
stack.append(start)
def valid(node):
    if node [0] in range (0,179) and node [1] in range (0,455):
        return True
    return False
def neighbors(img,node):#up,right,down,left
     up=node[0]-1,node[1]
     right=node[0],node[1]+1
     down=node[0]+1,node[1]
     left=node[0],node[1]-1
     if img[up]==0 and valid(up) :
         img[up]=100
         return img,up
     elif img[right]==0 and valid(right):
         img[right]=100
         return img,right
     elif img[down]==0 and valid(down):
         img[down]=100
         return img,down
     elif img[left]==0 and valid(left):
         img[left]=100
         return img,left
     return img,None
def depth(img,stack):
    a,next_node=neighbors(img,stack[-1])
    if next_node == None:
         stack.pop()
         return depth(a,stack)
    stack.append(next_node)
    b=stack[-1]
    if (b[0]==140 and b[1]==400):
         return stack
    return depth(a,stack)
a=depth(img,stack)
while a:
    print (a)
    b=a[-1]
    im[b[0],b[1]]=[0,255,255]
    a.pop()
cv2.imshow('Path',im)
cv2.waitKey(0)
     
    

