import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:\Image_processing\Image_processing\major\dog_bike_car.jpg")
plt.subplot(1, 1, 1)
plt.imshow(img)
plt.show()