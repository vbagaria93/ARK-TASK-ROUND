from cv2 import cv2 as cv2
def rescaleframe(frame1,):
   w=400
   q=500
   dimensions=(w,q)
   return cv2.resize(frame1,dimensions,interpolation=cv2.INTER_AREA)
cv2.imshow('b',cv2.add(rescaleframe(cv2.imread('atbash12.png')),rescaleframe(cv2.imread('Level1.png'))))
cv2.waitKey(0)