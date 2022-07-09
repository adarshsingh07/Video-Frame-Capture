import numpy as np
import cv2

cap=cv2.VideoCapture('Sample_Video1.mp4')
cv2.namedWindow("test")

img_counter = 0

while (True):
    ret, frame=cap.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE button is pressed for capturing the frames
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cap.release()
cv2.destroyAllWindows


