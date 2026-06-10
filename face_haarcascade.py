import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")  
smile_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")  

cap=cv2.VideoCapture(0)
ret,frame1= cap.read()
ret,frame2= cap.read()



while True:
    diff=cv2.absdiff(frame1,frame2)
    motion_gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(motion_gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for counter in contours:
        (x,y,w,h)=cv2.boundingRect(counter)

        if cv2.contourArea(counter)<2000:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),3)
 
    face_gray=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(face_gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=face_gray[y:y+h,x:x+w]
        roi_color=frame1[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        smiles=smile_cascade.detectMultiScale(roi_gray,1.5,15)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)

    cv2.imshow("Video",frame1)
    frame1=frame2
    ret,frame2= cap.read()
    if cv2.waitKey(1) & 0xFF == 27:
        break

   
cap.release()
cv2.destroyAllWindows()