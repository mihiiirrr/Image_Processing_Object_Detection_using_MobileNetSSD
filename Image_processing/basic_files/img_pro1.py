import cv2

print(cv2.__version__)

img= cv2.imread("D:/Image_processing/Image_processing/major/apple.jpg",0)
print(img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('apple_copy.png', img)