import numpy as np 
import cv2 

img = np.zeros((300,500,3), np.uint8)
# img = cv2.imread("poorva.jpg", 1 ) 

cv2.line(img,(0,10),(200,200), (0,0,255), 10)
cv2.arrowedLine(img,(0,0),(500,200), (0,255,0), 10)

cv2.circle(img,(250,100),100,(255,0,0), -1)
cv2.ellipse(img,(250,250),(100,50),0,0,360,(255,255,255),-1)

cv2.putText(img , 'POORVA', (50,50), cv2.FONT_HERSHEY_DUPLEX, 5, (255,255,0), 5 , cv2.LINE_8) 

cv2.ellipse(img,(250,250),(100,50),0,0,360,(255,255,255),-1)
cv2.imshow("poorva",img )
cv2.waitKey(0)

cv2.destroyAllWindows()

