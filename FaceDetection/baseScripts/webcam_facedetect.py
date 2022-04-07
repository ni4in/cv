import cv2


class FaceDetector:
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default2.xml') 
    
    def detect(self, image, scaleFactor= 1.1, minNeighbours = 5, minSize = (10,10)):
        rects = self.faceCascade.detectMultiScale(image, scaleFactor = scaleFactor, minNeighbors = minNeighbours, minSize = minSize, flags = cv2.CASCADE_SCALE_IMAGE)

        return rects 



cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("cannot open camera") 
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame, Exiting... ")
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    fd = FaceDetector()
    face_rects = fd.detect(gray)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('face', gray)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()         