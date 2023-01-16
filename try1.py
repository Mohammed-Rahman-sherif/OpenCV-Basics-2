import cv2
import numpy as np
from Stack import stack

frameWidth = 640
frameHeight = 480

img = cv2.VideoCapture(0)
img.set(3, frameWidth)
img.set(4, frameHeight)

while True:
	_, frame = img.read()
	kernel = np.ones((5,5),np.uint8)
	print(kernel)
	imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
	imgCanny = cv2.Canny(imgBlur,100,200)
	imgDilation = cv2.dilate(imgCanny,kernel , iterations = 2)
	imgEroded = cv2.erode(imgDilation,kernel,iterations=2)

	StackedImages = stack.stackImages(([img,imgGray,imgBlur],
                                   [imgCanny,imgDilation,imgEroded]),0.6)
	cv2.imshow("Staked Images", StackedImages)
	cv2.imshow("fr", frame)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break