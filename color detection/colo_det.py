import numpy as np 
import cv2

def empty(a):
	pass

frameWidth = 480
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

cv2.namedWindow("HSV")
cv2.resizeWindow('HSV', 640,280)
cv2.createTrackbar('HUE min','HSV', 0, 179, empty)
cv2.createTrackbar('HUE max','HSV', 179, 179, empty)
cv2.createTrackbar('SAT min','HSV', 0, 255, empty)
cv2.createTrackbar('SAT max','HSV', 255, 255, empty)
cv2.createTrackbar('VAL min','HSV', 0, 255, empty)
cv2.createTrackbar('VAL max','HSV', 255, 255, empty)

while  True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	h_min = cv2.getTrackbarPos('HUE min', 'HSV')
	h_max = cv2.getTrackbarPos('HUE max', 'HSV')
	s_min = cv2.getTrackbarPos('SAT min', 'HSV')
	s_max = cv2.getTrackbarPos('SAT max', 'HSV')
	v_min = cv2.getTrackbarPos('VAL min', 'HSV')
	v_max = cv2.getTrackbarPos('VAL max', 'HSV')

	#print(h_min)

	lower = np.array([h_min, s_min, v_min])
	upper = np.array([h_max, s_max, v_max])
	mask = cv2.inRange(hsv, lower, upper)
	result = cv2.bitwise_and(frame,frame, mask = mask)

	mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

	hstack = np.hstack([frame, result, mask])


	#cv2.imshow ('original', frame)
	#cv2.imshow ('mask', mask)
	#cv2.imshow ('result', result)
	#cv2.imshow ('HSVIMG', hsv)
	cv2.imshow ('Stacked Result', hstack)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()