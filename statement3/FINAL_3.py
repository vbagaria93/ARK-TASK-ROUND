
import numpy as np
from cv2 import cv2 as cv2
from scipy.io.wavfile import write
import pandas as pd
img1=cv2.imread('treasure_mp3.png')
img=cv2.cvtColor(cv2.imread('treasure_mp3.png'),cv2.COLOR_BGR2GRAY)
a=np.array(img1)
t=0
c=np.zeros((390*390,3),dtype='int16')
for i in range(0,390):
        for j in range (0,390):
                 c[t]=a[i][j]
                 t+=1
#k=np.linalg.norm(c)
e=(pd.DataFrame(c))
e.to_csv('final_prob.csv')
#c=c/k
write('newzz2.wav',44100,c)
#s='new1.wav'
#w='o.mp3'
#s1=AudioSegment.from_mp3(s)
#s1.export(w,format="wav")

