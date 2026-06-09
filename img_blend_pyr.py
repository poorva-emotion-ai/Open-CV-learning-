import cv2 
import numpy as np 

img=cv2.imread("white_rose.jpg",1)
img2=cv2.imread("red_rose.jpg",1)

img  = cv2.resize(img,  (500,500))
img2 = cv2.resize(img2, (500,500))

#Gaussian pyramid for red rose
layer=img.copy()
gp1=[layer]
for i in range (6):
    layer=cv2.pyrDown(layer)
    gp1.append(layer)
    cv2.imshow(str(i),layer)

#gaussian pyramid for whitee rose
icopy=img2.copy()
gp2=[icopy]
for i in range(6):
    icopy=cv2.pyrDown(icopy)
    gp2.append(icopy)
    cv2.imshow(str(i),icopy)

#Laplacian pyramid for red rose
layer=gp1[5]
for i in range(5,0,-1):
    gpup=cv2.pyrUp(gp1[i])
    gpup=cv2.resize(gpup,(gp1[i-1].shape[1],gp1[i-1].shape[0]))
    laplacian=cv2.subtract(gp1[i-1],gpup)
    cv2.imshow(str(i),laplacian)

#Laplacian pyramid for white rose
icopy=gp2[5]
for i in range(5,0,-1):
    gpup=cv2.pyrUp(gp2[i])
    gpup=cv2.resize(gpup,(gp2[i-1].shape[1],gp2[i-1].shape[0]))
    laplacian=cv2.subtract(gp2[i-1],gpup)
    cv2.imshow(str(i),laplacian)

#Now add left and right halves of the images in each level
lp1=[]
for i in range(5,0,-1):
    gpup=cv2.pyrUp(gp1[i])
    gpup=cv2.resize(gpup,(gp1[i-1].shape[1],gp1[i-1].shape[0]))
    laplacian=cv2.subtract(gp1[i-1],gpup)
    lp1.append(laplacian)

lp2=[]
for i in range(5,0,-1):
    gpup=cv2.pyrUp(gp2[i])
    gpup=cv2.resize(gpup,(gp2[i-1].shape[1],gp2[i-1].shape[0]))
    laplacian=cv2.subtract(gp2[i-1],gpup)
    lp2.append(laplacian)

LS=[]
for l1,l2 in zip(lp1,lp2):
    rows,cols,ch=l1.shape
    ls=np.hstack((l1[:,:cols//2], l2[:,cols//2:]))
    LS.append(ls)

ls_ = LS[0]

for i in range(1, len(LS)):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.resize(ls_, (LS[i].shape[1], LS[i].shape[0]))
    ls_ = cv2.add(ls_, LS[i])

cv2.namedWindow("Blended image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Blended image", 1000, 800)
cv2.imshow("Blended image",ls_)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()