import cv2 
import numpy as np 
import matplotlib.pyplot as plt

img=cv2.imread("white_rose.jpg")
b,g,r=cv2.split(img)


hist= plt.hist(b.ravel(),256,[0,256])
hist= plt.hist(g.ravel(),256,[0,256])
hist= plt.hist(r.ravel(),256,[0,256])
plt.show()

cv2.imshow("Original Image", img)
cv2.imshow("Original Image", b)
cv2.imshow("Original Image", g)
cv2.imshow("Original Image", r)
cv2.waitKey(0)
cv2.destroyAllWindows()
