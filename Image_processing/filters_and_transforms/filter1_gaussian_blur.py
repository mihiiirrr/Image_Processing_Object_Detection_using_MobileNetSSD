import cv2

image = cv2.imread("D:/Image_processing/Image_processing/major/16.jpg")

blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # (5, 5) is the kernel size, 0 is sigma (standard deviation)

cv2.imwrite('blurred_image.jpg', blurred_image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()