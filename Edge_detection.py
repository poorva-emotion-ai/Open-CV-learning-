import cv2 
import numpy as np 

img= cv2.imread("linux.png")

lap= cv2.Laplacian(img, cv2.CV_64F,ksize=5)
lap =np.uint8(np.absolute(lap))

sobelx= cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
sobely= cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)      
sobelx= np.uint8(np.absolute(sobelx))
sobely= np.uint8(np.absolute(sobely))   

cv2.imshow("img",img)
cv2.imshow("Laplacian", lap)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)   

cv2.waitKey(0)
cv2.destroyAllWindows()
