import cv2
import numpy as np

# harr cascades from https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

while True:
	ret = False
	while not ret:
		ret, img = cap.read()

	# Convert to grayscale to simplify image for search
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


	# Parameters for manipulating image data
	maxIntensity = 255.0
	phi = 1
	theta = 3 # TRY UPPING THETA IF TOO DARK

	# Attempt to make detection work in low light conditions	

	# Increase intensity such that
	# dark pixels become much brighter, 
	# bright pixels become slightly bright
	img_gray = (maxIntensity/phi)*(img_gray/(maxIntensity/theta))**0.5
	img_gray = np.array(img_gray,dtype='uint8')

	# Face detection using our haar cascade classifier
	faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.3, minNeighbors=8, minSize=(30,30))
	# faces = face_cascade.detectMultiScale(img_gray)

	roi_gray = None
	num = 0
	for (x, y, w, h) in faces:
		# Draw red rectangle over any roi identified as a face
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 4)
		roi_gray = img_gray[y:y+h, x:x+w]
		# roi_color = img[y:y+h, x:x+w]
	
		if not roi_gray is None:
			cv2.imshow('ROI detected as face(' + str(num) + ')', roi_gray)	

		num += 1

	cv2.imshow('Webcam stream tracking face', img)
	cv2.imshow('Edited grayscale', img_gray)
	#if not roi_gray is None:
	#	cv2.imshow('ROI matched to face', roi_gray)

	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
