import cv2
import numpy as np
img=cv2.imread("linux.png",-1)

kernal= np.ones((5,5),np.uint8)
dilation= cv2.dilate(img,kernal,iterations=2)
erosion= cv2.erode(img,kernal,iterations=2)

cv2.imshow("linux",img)
cv2.imshow("Dilation",dilation)
cv2.imshow("Erosion",erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
