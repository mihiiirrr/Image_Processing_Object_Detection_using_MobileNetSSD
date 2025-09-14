import cv2

# Read an image
image = cv2.imread("D:/Image_processing/Image_processing/major/apple.jpg")

# Apply Median filter
filtered_image = cv2.medianBlur(image, 5)

# Display the original and filtered image
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
