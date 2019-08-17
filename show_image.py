import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pikachu.jpg')
while True:
	cv2.imshow('Pikachu!', img)

	if cv2.waitKey(0):# & 0xFF == 27:
		break

cv2.destroyAllWindows()
