import cv2
import numpy
cap=cv2.VideoCapture(0)
while True:
	ret,frame=cap.read()	
	cv2.imshow('webcam',frame)
	c=cv2.waitKey(1)
	if c==27:
		break
cap.release()
cv2.destroyAllWindows()
