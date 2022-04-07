import cv2
from pyzbar.pyzbar import decode 
import numpy as np 


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("camera is not working, Exiting") 
    exit()

while True:
    ret,frame = cap.read()
    cv2.imwrite('qr.png',frame)
    if not ret :
        print("camera is not streaming. Exiting")
        break

    result = (decode(frame))
    if result:
        barcode_data = result[0].data
        barcode_type = result[0].type
        barcode_rect = result[0].rect 
        print(barcode_type)
        cv2.rectangle(frame, (barcode_rect.left, barcode_rect.top),(barcode_rect.left+barcode_rect.width,barcode_rect.top+barcode_rect.height),(0,255,0),2)
    else:
        print("No barcode detected")
    cv2.imshow('im',frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

