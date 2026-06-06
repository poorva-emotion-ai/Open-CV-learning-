import cv2 as cv 
import numpy as np 

img= cv.imread("linux.png")

kernel= np.ones((3,3),np.float32)/9
dist=cv.filter2D(img,-1,kernel)
blur=cv.blur(img,(3,3))
gblur=cv.GaussianBlur(img,(3,3),0)
median=cv.medianBlur(img,3) 
biletral=cv.bilateralFilter(img,9,5,5)


cv.imshow("img",img)
cv.imshow("dist",dist)
cv.imshow("blur",blur)
cv.imshow("gblur",gblur)
cv.imshow("median",median)
cv.imshow("biletral",biletral)

cv.waitKey(0)
cv.destroyAllWindows()

