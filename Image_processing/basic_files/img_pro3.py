import cv2

img= cv2.imread("D:/Image_processing/Image_processing/major/apple.jpg")

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()