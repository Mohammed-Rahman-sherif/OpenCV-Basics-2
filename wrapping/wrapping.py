import cv2
import numpy as np 

img = cv2.imread('C:\\Users\\smart\\Documents\\Computer Vision\\Basics\\feature_detection&classification\\thirukural.jpg')

height = 350
width = 250

pt1 = np.float32([[22,74],[107,30],[97,180],[192,134]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
print(pt1)

wrap = cv2.getPerspectiveTransform(pt1,pt2)
out = cv2.warpPerspective(img, wrap, (width,height))

for i in range (0,4):
	cv2.circle(img, (pt1[i][0],pt1[i][1]), 5, (0,255,0),cv2.FILLED)

cv2.imshow("img",img)
cv2.imshow("imgOut",out)
cv2.waitKey(0)