import cv2
import numpy as np

# Capture video from camera
vin = cv2.VideoCapture(0)
if not vin.isOpened():
	print('Camera source not found')

# Encoding
_fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = int(vin.get(cv2.CAP_PROP_FOURCC))
_framerate = vin.get(cv2.CAP_PROP_FPS)
_width = int(vin.get(cv2.CAP_PROP_FRAME_WIDTH))
_height = int(vin.get(cv2.CAP_PROP_FRAME_HEIGHT))

vout = cv2.VideoWriter('camera_capture.avi', _fourcc, _framerate, (_width,_height)) #(640,480))

while True:
	# res=success, frame=image of frame
	res, frame = vin.read()

	# Convert to grayscale
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Update video out stream with colored frame 
	vout.write(frame)
	
	cv2.imshow('original_capture', frame)
	cv2.imshow('grayscale_capture', frame_gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vin.release()
vout.release()
cv2.destroyAllWindows()
	
