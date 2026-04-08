


import cv2

def click_event(events,x,y,flags,params):
    if events == cv2.EVENT_RBUTTONDOWN:
        print(x,y)
        font = cv2.FONT_ITALIC
        strxy = str(x) + ',' + str(y)
        cv2.putText(img,strxy,(x,y), font,1, (0,255,0), 2)
        cv2.imshow('Panda',img)
    if events == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        font = cv2.FONT_ITALIC
        strxy = str(x) + ',' + str(y)
        cv2.putText(img,strxy,(x,y), font,1, (255,0,0), 2)
        cv2.imshow('Panda',img)
    if events ==cv2.EVENT_RBUTTONDBLCLK:
        blue = img[y,x,0]
        green = img[y,x,1]      
        red = img[y,x,2]
        font = cv2.FONT_ITALIC
        strxyz = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img,strxyz,(x,y), font,1, (0,0,255), 2)
        cv2.imshow('Panda',img)
 

img = cv2.imread('panda.jpg',1)
img = cv2.resize(img, (800, 600))
cv2.imshow('Panda',img)
cv2.setMouseCallback('Panda', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()



