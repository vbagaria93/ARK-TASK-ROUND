import numpy as np
from cv2 import cv2 as cv2
import math
import random
im=cv2.imread('MAZE_D.png')
img=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
img[140:155, 3:41] = 0
img[140:155, 400:441] = 0
start = [140, 41]
end = [140, 400]
def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()

    return points
def r_loc(img):
     x=random.randint(1,445)
     y=random.randint(1,159)
     if  img[y,x]!=0 :
         r_loc(img)
     return [y,x]
def dist_between_nodes(node1,node2):    #manhattan distance and the angle with the x axis
     y=abs(node1[0]-node2[0])
     x=abs(node1[1]-node2[1])
     if x!=0:
         ang=math.atan(y/x)
     else :
         ang=22/14
     return x+y,ang
def nearest_node(node_list,node):
    maxloc=0
    minval=1000
    for i in range (len(node_list)-1,0,-1):
        if (dist_between_nodes(node_list[i],node)[0]) < minval:
             minval=(dist_between_nodes(node_list[i],node)[0])
             maxloc=i
    return node_list[maxloc]
def next_find(img,node1,node2,steo=3):#node1 is the nearest node, node 2 is the random node
    a=get_line(node1[1],node1[0],node2[1],node2[0])
    if len(a)<=steo:
         steo=len(a)-1
    if steo<2:
        return 0
    for i in range (0,steo):
        b=a[i]
        if img[b[1],b[0]]==255:
            return next_find(img,node1,node2,i-1)
    q=a[steo]
    return q[1],q[0]
def planning(img,start,end,iter_len):
    nodelist=[start]
    nodetracker=[0]
    for i in range (0,iter_len):
         randomnode=r_loc(img)
         if img[randomnode[0],randomnode[1]]==255:
             continue
         nearnode=nearest_node(nodelist,randomnode)
         nextnode1=next_find(img,nearnode,randomnode)
         if(nextnode1==0):
             continue
         img[nextnode1[0],nextnode1[1]]=150
         nodelist.append(nextnode1)
         nodetracker.append(nodelist.index(nearnode))
         if nextnode1[0] in range (140,155) and nextnode1[1] in range (400,441):
             nodelist.append(end)
             nodetracker.append(nodelist.index(nearnode))
             return nodelist,nodetracker,img
    return None
nodelist,nodetracker,img=planning(img,start,end,500000)
def pathp(nodelist,nodetracker,b,im):
     a=nodelist[b]
     if (a[0]==140 and a[1]==41):
         return im
     im[a[0],a[1]]=[0,255,255]
     q=nodetracker[b]
     b=q
     return pathp(nodelist,nodetracker,b,im)
imaged=pathp(nodelist,nodetracker,-1,im)
cv2.imshow('Path',imaged)
cv2.waitKey(0) 