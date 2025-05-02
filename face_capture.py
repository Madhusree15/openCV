import cv2 as cv

face_cascade=cv.CascadeClassifier('haar_face.xml')

cap=cv.VideoCapture(0)

while True:
    _,img=cap.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)


    for (x,y,w,h) in faces_rect:
     cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Faces', img)

    k=cv.waitKey(30)&0xff
    if k==27:
       break
cap.release()