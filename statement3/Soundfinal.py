import pydub
from cv2 import cv2 as cv2
import numpy as np
img=cv2.cvtColor(cv2.imread('treasure.png'),cv2.COLOR_BGR2GRAY)
a=np.asarray(img)
def write(f, sr, x, normalized=False):
 
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")
write("final.mp3",320000,a)

    

