import cv2
import matplotlib.pyplot as plt

# Read in image to cv2 image
img = cv2.imread('pikachu.jpg')

# Read in grayscale image to cv2 image
img_grayscale = cv2.imread('pikachu.jpg', cv2.IMREAD_GRAYSCALE)

# Overlay rectangle
cv2.rectangle(img,(200,200),(600,600),(0,0,255),10)

# Show cv2 image
cv2.imshow('Pikachu!', img)
cv2.imshow('Pikachu grayscale!', img_grayscale)

# Wait until any key is pressed
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()

# Write cv2 image to jpg
cv2.imwrite('pikachu_gray.jpg', img_grayscale);

# open cv2 images with plt

# opencv BGR image to matplotlib RGB changes colors
# plt.imshow(img)
# plt.show()

# plt.imshow(img_grayscale, cmap='gray', interpolation='bicubic')
# plt.show()

