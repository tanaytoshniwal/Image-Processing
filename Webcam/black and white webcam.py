import cv2
import numpy
cap=cv2.VideoCapture(0)
while cap.isOpened():
	ret,frame=cap.read()
	frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('webcam',frame)
	c=cv2.waitKey(1)
	if c==27:
		break
cap.release()
cv2.destroyAllWindows()
