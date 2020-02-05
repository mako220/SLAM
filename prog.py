#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib.pyplot as plt 
#from matplotlib import pyplot as plt
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

cap = cv2.VideoCapture('test1.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    img = cv2.resize(frame , (1920//2,1080//2))

#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.mean(img, axis=2).astype(np.uint8)
    #print(img.shape)
    #print(img)
    corners = cv2.goodFeaturesToTrack(gray,maxCorners=1000,qualityLevel=0.01,minDistance=3)
#    corners = corners.astype(np.int)[:,0,:]
    corners = np.int0(corners)
    print(corners)
    for i in corners:
         x,y = i.ravel()
         cv2.circle(img,(x,y),3,(255,0,0),0)
    #cv2.imshow('video',img)
    #cv2.show()
    plt.imshow(img),plt.show()
    cv2.waitKey(25)
    continue
    if cv2.waitKey(0) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()





#using ssh
