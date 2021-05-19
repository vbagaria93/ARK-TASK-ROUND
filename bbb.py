import numpy as np
from cv2 import cv2 as cv2
original = cv2.cvtColor(cv2.imread('MAZE_D.png'), cv2.COLOR_BGR2GRAY)#blackandwhitepixels
og = cv2.imread('MAZE_D.png')#coloured pixels
stack1 = []  # width
stack2 = []  # height
marked = np.zeros((original.shape[1], original.shape[0]), dtype='uint8')
def dept(img, a):  # image and a list of the current coordinates
    global og
    global stack1
    global stack2
    global marked
    marked[a[1], a[0]] = 1
    stack1.append(a[1])
    stack2.append(a[0])
    og[a[1], a[0]] = [155, 132, 178]#to show that ive traversed via this
    if  a[0] > 138:  # terminating condition
        return 1
    p = visit(img, [a[0], a[1]], marked)
    for i in range(1, 5):
        if i != p:
            continue
        if p == 1:
            r = dept(img, [a[0] - 1,a[1]])
        elif p == 2:
            r = dept(img, [a[0] , a[1]+1])
        elif p == 3:
            r = dept(img, [a[0]+1, a[1]])
        elif p == 4:
            r = dept(img, [a[0], a[1]-1])
        if r == 1:
            return 1
    # backtrack
    og[a[1], a[0]] = [55, 182, 3]
    stack1.pop()
    stack2.pop()
    return 0
def visit(img, index, marked):
    if (img[index[1], index[0] - 1] == 0) & marked[index[1], index[0] - 1] == 0:
        return 1
    elif (img[index[1]+ 1, index[0]] == 0) & marked[index[1] + 1, index[0]] == 0:
        return 2
    elif (img[index[1], index[0] + 1] == 0) & marked[index[1], index[0] + 1] == 0:
        return 3
    elif (img[index[1] - 1, index[0]] == 0) & marked[index[1] - 1, index[0]] == 0:
        return 4
    else:
        return 0  # bashes EOF
if (dept(original, [137,9]) == 1):
    cv2.imshow('found', og)
cv2.waitKey(0)