from cv2 import cv2 as cv2
import numpy as np
class node1:
    def __init__(self,abscissa,ordinate):
        self.x=abscissa
        self.y=ordinate
        self.d=float('inf') #distance from source
        self.parent_x=None
        self.parent_y=None
        self.processed=False
        self.ind__in_stack=None
im=cv2.imread('MAZE_D.png')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
img[140:155, 3:41] = 0
img[140:155, 400:441] = 150
start = [140, 41]
end = [140, 400]
def transfer_up(stack, ind_):
     track_n=(ind_-1)//2
     if ind_ == 0:
         return stack
     if stack[ind_].d < stack[track_n].d:
         a=stack[ind_]
         stack[ind_]=stack[track_n]
         stack[track_n]=a
         stack[ind_].ind__in_stack=ind_
         stack[track_n].ind__in_stack=track_n
         stack = transfer_up(stack, track_n)
     return stack
     #a=stack[ind_]
     #stack[ind_]=stack[0]
     #stack[0]=a
     #return stack    
def transfer_down(stack, ind_):
    length=len(stack)
    lc_ind_=2*ind_+1
    rc_ind_=lc_ind_+1
    if lc_ind_ >= length:
        return stack
    if lc_ind_ < length and rc_ind_ >= length:
        if stack[ind_].d > stack[lc_ind_].d:
            stack[ind_], stack[lc_ind_]=stack[lc_ind_], stack[ind_]
            stack[ind_].ind__in_stack=ind_
            stack[lc_ind_].ind__in_stack=lc_ind_
            stack = transfer_down(stack, lc_ind_)
    else:
        small = lc_ind_
        if stack[lc_ind_].d > stack[rc_ind_].d:
            small = rc_ind_
        if stack[small].d < stack[ind_].d:
            stack[ind_],stack[small]=stack[small],stack[ind_]
            stack[ind_].ind__in_stack=ind_
            stack[small].ind__in_stack=small
            stack = transfer_down(stack, small)
    return stack
def get_livestack(mat,r,c):
    shape=mat.shape
    livestack=[]
    #ensure neighbors are within image boundaries
    if r > 0 and not mat[r-1][c].processed:
         livestack.append(mat[r-1][c])
    if r < shape[0] - 1 and not mat[r+1][c].processed:
            livestack.append(mat[r+1][c])
    if c > 0 and not mat[r][c-1].processed:
        livestack.append(mat[r][c-1])
    if c < shape[1] - 1 and not mat[r][c+1].processed:
            livestack.append(mat[r][c+1])
    return livestack
def get_distance(img,u,v):#returns the eucldiean distance of the pixels, which if different indicate conflict
    return 1+ (float(img[v][0])-float(img[u][0]))**2+(float(img[v][1])-float(img[u][1]))**2
def pathp(img,path):
    x0,y0=path[0]
    for node1 in path[1:]:
        x1,y1=node1
        cv2.line(img,(x0,y0),(x1,y1),(0,255,255),thickness=2)
        x0,y0=node1
def next_node(img,src,dst):
    pq=[] 
    source_x,source_y=src[0],src[1]
    dest_x,dest_y=dst[0],dst[1]
    row,imagecols=img.shape[0],img.shape[1]
    matrix = np.full((row, imagecols), None) #access by matrix[row][col]
    for r in range(row):
        for c in range(imagecols):
            matrix[r][c]=node1(c,r)
            matrix[r][c].ind__in_stack=len(pq)
            pq.append(matrix[r][c])
    matrix[source_y][source_x].d=0
    pq=transfer_up(pq, matrix[source_y][source_x].ind__in_stack)
    while len(pq):
        u=pq[0]
        u.processed=True
        pq[0]=pq[-1]
        pq[0].ind__in_stack=0
        pq.pop()
        pq=transfer_down(pq,0)
        livestack = get_livestack(matrix,u.y,u.x)
        for v in livestack:
            dist=get_distance(img,(u.y,u.x),(v.y,v.x))
            if u.d + dist < v.d:
                v.d = u.d+dist
                v.parent_x=u.x
                v.parent_y=u.y
                idx=v.ind__in_stack
                pq=transfer_down(pq,idx)
                pq=transfer_up(pq,idx)                          
    path=[]
    iter_v=matrix[dest_x][dest_y]
    path.append((dest_x,dest_y))
    while(iter_v.y!=source_y or iter_v.x!=source_x):
        path.append((iter_v.x,iter_v.y))
        iter_v=matrix[iter_v.parent_y][iter_v.parent_x]

    path.append((source_x,source_y))
    return path
p=next_node(im,(start[1],start[0]),end)
pathp(im,p)
cv2.imshow('path',im)
cv2.waitKey(0)
