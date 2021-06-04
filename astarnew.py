from cv2 import cv2 as cv2
import numpy as np
im=cv2.imread('MAZE_D.png')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
img[140:155, 3:41] = 0
img[140:155, 400:441] = 150
start = [140, 41]
end = [140, 400]
class Vertex:#Helper functions and classes
    def __init__(self,x_coord,y_coord):
        self.x=x_coord
        self.y=y_coord
        self.d=float('inf') #distance from source
        self.parent_x=None
        self.parent_y=None
        self.processed=False
        self.index_in_queue=None
#Return neighbor directly above, below, right, and left
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
def bubble_up(queue, index):
     if index == 0:
         return queue
     p_index=(index-1)//2
     if queue[index].d < queue[p_index].d:
         a=queue[index]
         queue[index]=queue[p_index]
         queue[p_index]=a
         queue[index].index_in_queue=index
         queue[p_index].index_in_queue=p_index
         queue = bubble_up(queue, p_index)
     return queue
     #a=queue[index]
     #queue[index]=queue[0]
     #queue[0]=a
     #return queue    
def bubble_down(queue, index):
    length=len(queue)
    lc_index=2*index+1
    rc_index=lc_index+1
    if lc_index >= length:
        return queue
    if lc_index < length and rc_index >= length: #just left child
        if queue[index].d > queue[lc_index].d:
            queue[index], queue[lc_index]=queue[lc_index], queue[index]
            queue[index].index_in_queue=index
            queue[lc_index].index_in_queue=lc_index
            queue = bubble_down(queue, lc_index)
    else:
        small = lc_index
        if queue[lc_index].d > queue[rc_index].d:
            small = rc_index
        if queue[small].d < queue[index].d:
            queue[index],queue[small]=queue[small],queue[index]
            queue[index].index_in_queue=index
            queue[small].index_in_queue=small
            queue = bubble_down(queue, small)
    return queue
def get_distance(img,u,v):#returns the eucldiean distance of the pixels, which if different indicate conflict
    return 1+ (float(img[v][0])-float(img[u][0]))**2+(float(img[v][1])-float(img[u][1]))**2
def drawPath(img,path):
    '''path is a list of (x,y) tuples'''
    x0,y0=path[0]
    for vertex in path[1:]:
        x1,y1=vertex
        cv2.line(img,(x0,y0),(x1,y1),(90,40,230),thickness=4)
        x0,y0=vertex

def find_shortest_path(img,src,dst):
    pq=[] #min-heap priority queue
    source_x=src[0]
    source_y=src[1]
    dest_x=dst[0]
    dest_y=dst[1]
    imagerows,imagecols=img.shape[0],img.shape[1]
    matrix = np.full((imagerows, imagecols), None) #access by matrix[row][col]
    for r in range(imagerows):
        for c in range(imagecols):
            matrix[r][c]=Vertex(c,r)
            matrix[r][c].index_in_queue=len(pq)
            pq.append(matrix[r][c])
    matrix[source_y][source_x].d=0
    pq=bubble_up(pq, matrix[source_y][source_x].index_in_queue)
    while len(pq):
        u=pq[0]
        u.processed=True
        pq[0]=pq[-1]
        pq[0].index_in_queue=0
        pq.pop()
        pq=bubble_down(pq,0)
        livestack = get_livestack(matrix,u.y,u.x)
        for v in livestack:
            dist=get_distance(img,(u.y,u.x),(v.y,v.x))
            if u.d + dist < v.d:
                v.d = u.d+dist
                v.parent_x=u.x
                v.parent_y=u.y
                idx=v.index_in_queue
                pq=bubble_down(pq,idx)
                pq=bubble_up(pq,idx)                          
    path=[]
    iter_v=matrix[dest_x][dest_y]
    path.append((dest_x,dest_y))
    while(iter_v.y!=source_y or iter_v.x!=source_x):
        path.append((iter_v.x,iter_v.y))
        iter_v=matrix[iter_v.parent_y][iter_v.parent_x]

    path.append((source_x,source_y))
    return path
p=find_shortest_path(im,(start[1],start[0]),end)
drawPath(im,p)
cv2.imshow('path',im)
cv2.waitKey(0)
