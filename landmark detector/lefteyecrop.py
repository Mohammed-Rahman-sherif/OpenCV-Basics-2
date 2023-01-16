import cv2
import dlib
import numpy as np 

def createBox(img, points, scale = 5):
	bbox = cv2.boundingRect(points)
	x, y, w, h = bbox
	imgCrop = img[y:y+h, x:x+w]
	imgCrop = cv2.resize(imgCrop, (0,0), None, scale, scale)
	return imgCrop

img = cv2.imread('elon.jpg')
img = cv2.resize(img, (0,0), None, 0.7,0.7)
imgoriginal = img.copy()

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detector(gray)

for face in faces:
	x1,y1 = face.left(), face.top()
	x2,y2 = face.right(), face.bottom()
#	imgoriginal = cv2.rectangle(img, (x1,y1),(x2,y2), (255,0,0), 2)
	landmarks = predictor(gray, face)
	myPoints = []
	for n in range(68):
		x = landmarks.part(n).x
		y = landmarks.part(n).y
		myPoints.append([x,y])
		cv2.circle(imgoriginal, (x,y), 4,(0,255,0),cv2.FILLED)
		cv2.putText(imgoriginal, str(n), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255,0,0), 1)

	myPoints = np.array(myPoints)
	leftEye = createBox(img, myPoints[36:42])
	cv2.imshow('LeftEye', leftEye)

	print(myPoints)
cv2.imshow('img', imgoriginal)
cv2.waitKey(0)