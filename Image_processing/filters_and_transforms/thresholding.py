import cv2

image = cv2.imread("D:/Image_processing/Image_processing/major/16.jpg", cv2.IMREAD_GRAYSCALE)
threshold_value = 127
max_value = 255

# Apply thresholding
_, thresholded_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

# Display the original and thresholded image
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
