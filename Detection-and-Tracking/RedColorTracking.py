import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened():
	ret,frame=cap.read()
	red = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), np.array([136,87,111]), np.array([180,255,255]))
	(ret,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic,contour in enumerate(contours):
		area=cv2.contourArea(contour)
		if(area>300):
			x,y,w,h=cv2.boundingRect(contour)
			frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.circle(frame, (x+int(w/2),y+int(h/2)),  1, 0, 3)
			distance1=int((int(int(cap.get(3))/2)-x+int(w/2)))
			distance2=int((int(int(cap.get(4))/2)-y+int(h/2)))
			print ("( "+str(distance1)+" , "+str(distance2)+" )")
	cv2.imshow('frame',frame)
	if cv2.waitKey(5) == 27:
		cv2.destroyAllWindows()
		cap.release()
		break
