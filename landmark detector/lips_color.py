import cv2
import dlib
import numpy as np 

webcam = True

cap = cv2.VideoCapture(0)

def createBox(img, points, scale = 5, masked = False, cropped = True):
	if masked:
		mask = np.zeros_like(img)
		mask = cv2.fillPoly(mask, [points], (255,255,255))

		img = cv2.bitwise_and(img, mask)
		#cv2.imshow('mask', img)

	if cropped:
		bbox = cv2.boundingRect(points)
		x, y, w, h = bbox
		imgCrop = img[y:y+h, x:x+w]
		imgCrop = cv2.resize(imgCrop, (0,0), None, scale, scale)
		return imgCrop

	else:
		return mask

def empty(a):
	pass

cv2.namedWindow('BGR')
cv2.resizeWindow('BGR', 640, 240)
cv2.createTrackbar('BLUE', 'BGR', 0, 255, empty)
cv2.createTrackbar('GREEN', 'BGR', 0, 255, empty)
cv2.createTrackbar('RED', 'BGR', 0, 255, empty)

while 1:
	if webcam:
		success, img = cap.read()
	
	else:
		img = cv2.imread('2.jfif')
	img = cv2.resize(img, (0,0), None, 1,1)
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
			#cv2.circle(imgoriginal, (x,y), 4,(0,255,0),cv2.FILLED)
			#cv2.putText(imgoriginal, str(n), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255,0,0), 1)

		myPoints = np.array(myPoints)
		#leftEye = createBox(img, myPoints[36:42])
		lips = createBox(img, myPoints[48:60],3,masked=True,cropped = False)
		lipscol = np.zeros_like(lips)

		b = cv2.getTrackbarPos('BLUE', 'BGR')
		g = cv2.getTrackbarPos('GREEN', 'BGR')
		r = cv2.getTrackbarPos('RED', 'BGR')

		lipscol[:] = b,g,r
		lipscol = cv2.bitwise_and(lips,lipscol)
		lipscol = cv2.GaussianBlur(lipscol,(7,7),10)
		lipscol = cv2.addWeighted(imgoriginal, 1, lipscol, 0.4, 0)

		cv2.imshow('BGR', lipscol) 

		#cv2.imshow('Lips_Original', lips)

		#print(myPoints)
	cv2.imshow('img', imgoriginal)
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()