import numpy as np 
import cv2

def click_event(event , x , y , flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img,(x,y),3,(255,255,0),-1)    
        
        mycolorImage= np.zeros((512,512,3),np.uint8)
        mycolorImage[:]=[blue,green ,red]
        cv2.imshow('colorimage',mycolorImage)
     
    
#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("D:/Image_processing/Image_processing/major/apple.jpg")
cv2.imshow('image',img)
points= []
cv2.setMouseCallback('image',click_event)

cv2.waitKey()
cv2.destroyAllWindows()