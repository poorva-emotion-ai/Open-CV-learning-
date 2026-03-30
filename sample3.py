import cv2
cap = cv2.VideoCapture("sea.mp4",0)
forcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi",forcc,10.0,(600,350))


while True:
    ret, frame = cap.read()
    if ret ==False:
        break 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", gray)
    out.write(gray)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

