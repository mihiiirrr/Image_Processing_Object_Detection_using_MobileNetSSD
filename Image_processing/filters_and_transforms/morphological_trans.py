import cv2
import numpy as np

# Read the input image (grayscale)
image = cv2.imread("D:/Image_processing/Image_processing/major/apple.jpg", 0)

# Define a rectangular kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Perform dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Perform erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Perform morphological gradient (dilation - erosion)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Display the results
cv2.imshow('Dilated Image', dilated)
cv2.imshow('Eroded Image', eroded)
cv2.imshow('Morphological Gradient', gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
