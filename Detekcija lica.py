##U�itava se numpy i OpenCV
import numpy as np
import cv2

#U�itavanje Haar-ovih kaskada
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#lista sa slikama na kojima se prepoznaje lice
slike = ['lice.jpg', 'lena.jpg', 'repka.jpg']

for i in range(len(slike)):
    #U�itavanje slike i pretvaranje slike u sivu
    naziv_slike = slike[i]
    img = cv2.imread(naziv_slike)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #tra�i se odre�eni dijelovi lica i uokviruju se razli�itim bojama
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    

    naziv_slike = naziv_slike.split('.')[0]
    #prikazuje se slika
    cv2.imshow(naziv_slike,img)
#zatvara se aplikacija
cv2.waitKey(0)
cv2.destroyAllWindows()
