import cv2
import dlib
import numpy as np 

img = cv2.imread('C:\\Users\\smart\\Pictures\\opencv images\\lena.jfif')
img = cv2.resize(img, (0,0), None, 3,3)
imgoriginal = img.copy()

detector = dlib.get_frontal_face_detector()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detector(gray)

for face in faces:
	x1,y1 = face.left(), face.top()
	x2,y2 = face.right(), face.bottom()
	imgoriginal = cv2.rectangle(img, (x1,y1),(x2,y2), (255,0,0), 2)

cv2.imshow('img', imgoriginal)
cv2.waitKey(0)