import cv2

class FaceDetector():
    def __init__(self):
        self.cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def detect(self, image, scale_factor=1.1, min_neighbor = 5, min_size =(10,10)):
        rects = self.cascade.detectMultiScale(image, scaleFactor= scale_factor,minNeighbors=min_neighbor,minSize=min_size,flags = cv2.CASCADE_SCALE_IMAGE)
        return rects 



