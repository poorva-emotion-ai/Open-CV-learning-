

import numpy as np
import cv2

def click_event(events,x,y,flags,params):
    if events == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        mycolorimage = np.zeros((512,512,3),np.uint8)
        mycolorimage[:] = [blue,green,red]
        cv2.imshow('Color',mycolorimage)    
   
 

img = cv2.imread('panda.jpg',1)
img = cv2.resize(img, (800, 600))
cv2.imshow('Panda',img)
cv2.setMouseCallback('Panda', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()



