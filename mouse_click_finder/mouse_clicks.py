import cv2
import numpy as np 

circle = np.zeros((4, 2),np.int)
counter = 0

def mouseclick(event, x, y, flags, params):
	global counter
	if event == cv2.EVENT_LBUTTONDOWN:
		circle[counter] = x, y
		counter = counter + 1
		print(circle)

img = cv2.imread('C:\\Users\\smart\\Documents\\Computer Vision\\Basics\\feature_detection&classification\\thirukural.jpg')
img = cv2.resize(img, (0,0), None, 0.5,0.5)
while True:

	if counter == 4:
		
		width = 640		
		height = 480
		pt1 = np.float32([circle[0],circle[1],circle[2],circle[3]])
		pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

		wrap = cv2.getPerspectiveTransform(pt1,pt2)
		out = cv2.warpPerspective(img, wrap, (width,height))
		cv2.imshow('image', out)

	for i in range (0,4):
		cv2.circle(img, (circle[i][0], circle[i][1]), 5, (0,255,0),cv2.FILLED)

	cv2.imwrite('thirukural1.jpg', img)
	cv2.imshow("img", img)
	cv2.setMouseCallback("img", mouseclick)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break