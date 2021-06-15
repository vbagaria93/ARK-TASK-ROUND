import numpy as np
from cv2 import cv2


cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    xyg=cv2.GaussianBlur(frame,(3,3),4000,2200,cv2.BORDER_DEFAULT)
    xyg=cv2.flip(xyg,1)
    xyg=cv2.cvtColor(xyg,cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    
    
    hc=cv2.CascadeClassifier(os.path.expanduser("~/Desktop/somefile.tx")
    fr=hc.detectMultiScale(xyg,1.1,3)
    print( 'no of face found are : {len(fr)}' + len(fr))
    for(x,y,w,h) in fr:
        cv2.circle(xyg,((x+w)//2,((y+h)//2),h//2,(0,255,0),3)

    cv2.imshow('frame',xyg)  
    if cv2.waitKey(20) & 0xFF == ord('d'):
       break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()