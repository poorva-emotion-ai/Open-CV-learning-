import cv2 
import numpy as np 

img=cv2.imread("panda.jpg")
img2= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY,img)

ret, thresh =cv2.threshold(img2,125,255,0)
counters,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("Number of counters are= ",len(counters))

cv2.drawContours(img,counters,-1,(0,255,0),3)

cv2.imshow("Original Image",img)
cv2.imshow("Gray Image",img2)   
cv2.waitKey(0)
cv2.destroyAllWindows()