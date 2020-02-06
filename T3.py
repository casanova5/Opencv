import cv2
#cam = cv2.VideoCapture('output.avi') #if != camera
cam = cv2.VideoCapture(0)
facedata = cv2.CascadeClassifier('face.xml')
eyedata = cv2.CascadeClassifier('eye.xml')

while 3>2:
    x,y=cam.read() #status,frame
    print(y) #coordinates ayengey isse
    facecord= facedata.detectMultiScale(y)
    print(facecord) #face k coordinate print hongey
    for (x1,y1,w,h) in facecord:
        cv2.rectangle(y,(x1,y1),(x1+w,y1+h),(0,100,100),5)  #BGR
        f=y[y1:y1+h,x1:x1+w]
        #cv2.imshow('face',f)
        eye= eyedata.detectMultiScale(f)
        cv2.imshow('eyed',eye)
    cv2.imshow('class',y)
    #cv2.imshow('eyed',eye)
    #cv2.imshow('face',f)
    if cv2.waitKey(5) & 0xff == ord('q'):
        break