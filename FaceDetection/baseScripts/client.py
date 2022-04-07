import cv2
import numpy as np 
import requests 
import base64


im = cv2.imread('face3.jpeg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
gray_bytes = gray.tobytes()
im_string = base64.b64encode(gray_bytes).decode('utf8')
(m,n) = gray.shape
url = 'http://127.0.0.1:5000/face'
data = {'image':im_string,'xres': n,'yres':m} 
res = requests.post(url,json=data)
bbox_list = res.json()["faces"]
for bbox in bbox_list:
    cv2.rectangle(im,(bbox["x"],bbox["y"]),(bbox["x"]+bbox["w"], bbox["y"]+bbox["h"]),(0,255,0),2)

cv2.imshow('frame',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
    