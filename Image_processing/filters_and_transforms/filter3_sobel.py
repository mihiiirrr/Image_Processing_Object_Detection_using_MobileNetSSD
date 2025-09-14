import cv2
import numpy as np

# Read an image in grayscale
image = cv2.imread("D:/Image_processing/Image_processing/major/apple.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Sobel filter
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Display the original and Sobel-filtered image

cv2.imshow('Sobel Filtered Image', np.uint8(sobel_combined))
cv2.waitKey(0)
cv2.destroyAllWindows()
