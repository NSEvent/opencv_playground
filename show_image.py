import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read in image
img = cv2.imread('pikachu.jpg')

# Read in grayscale image
img_grayscale = cv2.imread('pikachu.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Pikachu!', img)
cv2.imshow('Pikachu grayscale!', img_grayscale)

cv2.waitKey(0)
cv2.destroyAllWindows()


# opencv BGR image to matplotlib RGB changes colors
plt.imshow(img)
plt.show()

plt.imshow(img_grayscale, cmap='gray', interpolation='bicubic')
plt.show()

