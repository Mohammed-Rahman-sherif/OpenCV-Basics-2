import cv2
import numpy as np 

img1 = cv2.imread('imgQuery/thirukural.jpg')
img2 = cv2.imread('imgTrain/thirukural.jpg')
img2 = cv2.resize(img2, (0,0), None, 0.5,0.5)

orb = cv2.ORB.create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

imgkp1 = cv2.drawKeypoints(img1, kp1, None)
imgkp2 = cv2.drawKeypoints(img2, kp2, None)

cv2.imshow('imgkp1',imgkp1)
cv2.imshow('imgkp2',imgkp2)
#cv2.imshow('img1', img1)
#cv2.imshow('img2', img2)

cv2.waitKey(0)