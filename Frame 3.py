#Exracts every frame from an video

import numpy as np
import cv2 
import os

cap=cv2.VideoCapture('Sample_Video1.mp4')

count = 0
success = 1

if not os.path.exists('data'):
    os.makedirs('data')

while success:
    ret, frame=cap.read()
    cv2.imwrite("frame%d.jpg" % count, frame)    
    count += 1
    
cap.release()
cv2.destroyAllWindows


