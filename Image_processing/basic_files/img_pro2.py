import cv2
import numpy as np 


print(cv2.__version__)

img= cv2.imread("D:/Image_processing/Image_processing/major/apple.jpg",1)
#img= np.zeros((512,512,3), np.uint8)

img = cv2.line(img,(0,0),(255,255), (0,0,255), 15)

img = cv2.arrowedLine(img,(0,100),(100,200), (0,255,0), 5)

img = cv2.rectangle(img,(385,0),(510,128),(255,0,0),10)

img = cv2.circle(img ,(447,63),63,(255,0,255) ,-1)

font=cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OPEN-CV',(10,500),font , 3,(0,255,255) ,10,cv2.LINE_8)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()