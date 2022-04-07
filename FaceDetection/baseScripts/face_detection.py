import cv2 
import numpy as np 
import argparse


class FaceDetector:
    def __init__(self,  faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath) 
    
    def detect(self, image, scaleFactor= 1.1, minNeighbours = 5, minSize = (10,10)):
        rects = self.faceCascade.detectMultiScale(image, scaleFactor = scaleFactor, minNeighbors = minNeighbours, minSize = minSize, flags = cv2.CASCADE_SCALE_IMAGE)

        return rects 

ap = argparse.ArgumentParser()
ap.add_argument("-f","--face", required=True, help = "path to where the face cascade resides")
ap.add_argument("-i", "--image", required = True, help = "path to where the image file resides")
args = ap.parse_args()

image = cv2.imread(args.image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fd = FaceDetector(args.face)
face_rects = fd.detect(gray)
print("found {} of faces".format(len(face_rects))) 

for (x,y,w,h) in face_rects:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Faces", image)
cv2.waitKey(0) 



