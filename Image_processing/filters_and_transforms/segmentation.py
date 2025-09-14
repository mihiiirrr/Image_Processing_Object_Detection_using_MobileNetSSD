import cv2
import numpy as np

# Read the input image
image = cv2.imread("D:/Image_processing/Image_processing/major/16.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

# Find contours in the edged image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Display the results
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
