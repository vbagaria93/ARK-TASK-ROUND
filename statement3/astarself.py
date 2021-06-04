from queue import PriorityQueue
from cv2 import cv2 as cv2
import numpy as np
from numpy.lib.function_base import append
im = cv2.imread('MAZE_D.png')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
img[140:155, 3:41] = 0
img[140:155, 400:441] = 150
start = [140, 41]
end = [140, 400]  # start and end positions of the maze

def neighbors(node, img):
    stack = []
    up = (node[0] - 1, node[1])
    right = (node[0], node[1] + 1)
    down = (node[0] + 1, node[1])
    left = (node[0], node[1] - 1)
    if (img[up] != 255):
        stack.append(up)
    if (img[right] != 255):
        stack.append(right)
    if (img[down] != 255):
        stack.append(down)
    if (img[left] != 255):
        stack.append(left)
    return stack


def hvalue(node, end):
    return (abs(node[0] - end[0]) + abs(node[1] - end[1]))


def retrace(came_from, im):
    d=len(came_from)
    for d in range(0,d):
        a=came_from[d]
        im[a[0],a[1]] = [0, 225,225]
    return im


def astar(start, end, img, im):
    c = 0
    d = 1
    tracker = PriorityQueue()  # three arguments namely,fvalue of the neighbour,counter,lastnode
    tracker.put([hvalue(start, end), c, start])
    came_from = [start]
    gvalue = np.zeros((img.shape[0], img.shape[1]))
    fvalue = np.zeros((img.shape[0], img.shape[1]))
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            gvalue[i][j] = float("inf")
            fvalue[i][j] = float("inf")
    gvalue[start[0],start[1]]=0
    fvalue[start[0],start[1]] = hvalue(start, end)
    currenthash = [start]
    while not tracker.empty() :
        currentnode = tracker.get()[2]
        currenthash.remove(currentnode)
        if currentnode == end:
            im=retrace(came_from, im)
            cv2.imshow('print',im)
            return True
        q = neighbors (currentnode, img)
        for i in range(0, len(q)):
            temp = gvalue[currentnode[0],currentnode[1]] + 1
            a=q[i]
            if temp < gvalue[a[0],a[1]]:
                came_from.append(q[i])
                d+=1
                gvalue[a[0],a[1]] = temp
                fvalue[a[0],a[1]] = temp + hvalue(q[i], end)
                if q[i] not in currenthash:
                    c += 1
                    tracker.put([fvalue[q[i]], c, q[i]])
                    currenthash.append(q[i])
    return False


if astar(start, end, img, im):
     print(astar(start, end, img, im))
cv2.waitKey(0)
