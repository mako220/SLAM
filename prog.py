#!/usr/bin/env python3

import cv2
import numpy as np


cap = cv2.VideoCapture('test1.mp4')

#def nothing(x):
#    pass

cv2.namedWindow("Frame")
#cv2.createTrackbar("quality","Frame", 1, 100,nothing)

while(cap.isOpened()):
    _, frame = cap.read()

    img = cv2.resize(frame , (1920//2,1080//2))

    gray = np.mean(img, axis=2).astype(np.uint8)
    #print(img.shape)
    #print(img)
    corners = cv2.goodFeaturesToTrack(gray,maxCorners=1000,qualityLevel=0.01,minDistance=3)
    corners = np.int0(corners)

    print(corners)
    for i in corners:
         x,y = i.ravel()
         cv2.circle(img,(x,y),3,(255,0,0),-1)
   
    cv2.imshow("Frame", img)
    key = cv2.waitKey(1)
    if key == 27:
         break

cap.release()
cv2.destroyAllWindows()





#using ssh
