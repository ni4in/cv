from flask import Flask
from flask_restful import Resource,Api,reqparse
from face_detector import FaceDetector 
import base64 
import numpy as np 
import cv2
# flask definition 
app = Flask(__name__)
# initializing an API 
api = Api(app)        
# defining the Image resource class via inheritence
class Image(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('image',type = str, required = 'True', help = 'this field cannot be empty' )
    parser.add_argument('xres', type = int, required = 'True', help = 'this field cannot be empty')
    parser.add_argument('yres', type = int, required = 'True', help = 'this field cannot be empty')

    def post(self):
        data = Image.parser.parse_args()
        im_string = data['image']
        m = data['yres']
        n = data['xres']
        im_bytes = base64.b64decode(im_string.encode('utf8'))
        im_array = np.frombuffer(im_bytes, dtype='uint8')
        im = im_array.reshape((m,n)) 
        cv2.imwrite('k.png', im)
        detector = FaceDetector()
        face_rects = detector.detect(im)
        detections = []
        for (x,y,w,h) in face_rects: 
            detections.append({"x":int(x),"y":int(y),"w":int(w),"h":int(h)})
        return {"faces":detections}
api.add_resource(Image,'/face')
app.run(port = 5000, debug='True')


