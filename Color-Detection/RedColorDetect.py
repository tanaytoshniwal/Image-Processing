import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True :
	ret,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	redl=np.array([136,87,111])
	redu=np.array([180,255,255])
	red=cv2.inRange(hsv,redl,redu)
	cv2.imshow("color detect",red)
	if cv2.waitKey(5) == 27:
		break 
cv2.destroyAllWindows()
cap.release()
