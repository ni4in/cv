import cv2
import numpy as numpy
import pyzbar.pyzbar as pyzbar 
import matplotlib.pyplot as plt 

im = cv2.imread('book.jpg')
def decode(im):
    decoded_objects = pyzbar.decode(im)
    return decoded_objects

result = (decode(im))

barcode_data = result[0].data
barcode_type = result[0].type
barcode_rect = result[0].rect
print(barcode_data, barcode_rect, barcode_type) 
cv2.rectangle(im, (barcode_rect.left, barcode_rect.top),(barcode_rect.left+barcode_rect.width,barcode_rect.top+barcode_rect.height),(0,255,0),2)
cv2.imshow('im',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.rectangle(im, pt1, pt2, color)   



