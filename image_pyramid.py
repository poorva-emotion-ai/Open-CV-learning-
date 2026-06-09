import cv2 
import numpy as np 

img=cv2.imread('rabbit.jpg')
icopy= img.copy()

gp=[icopy]

for i in range(6):
    icopy=cv2.pyrDown(icopy)
    gp.append(icopy)
    #cv2.imshow(str(i),icopy)

layer=gp[5]
cv2.imshow("Upperlevel of gaussian pyramid",layer)


for i in range (5,0,-1):
    gpyramid= cv2.pyrUp(gp[i])
    #to make the size of the image same as the previous level of the pyramid    
    gpyramid = cv2.resize(
        gpyramid,
        (gp[i-1].shape[1], gp[i-1].shape[0]))
    
    laplacian=cv2.subtract(gp[i-1],gpyramid)
    cv2.imshow(str(i),laplacian)


cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()