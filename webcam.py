import cv2
import numpy as np
import os
from color_transfer import color_transfer
video_capture = cv2.VideoCapture(0)
x= True
def fil():
    a=[]
    for _,_,f in os.walk("filter"):
        a.append(f)
    
    return a[0]
l=0
affect=None
def nex(l=0,step='f'):
    t=fil()
    if step=='f':
        l+=1
        l=l%len(t)
        img=cv2.imread("filter/"+str(t[l]))
        return img,l
    else:
        l-=1
        img=cv2.imread("filter/"+str(t[l]))
        l=l%len(t)
        return img,l
bueaty=False
while x:
    ret, image = video_capture.read()
    if ret:
        if bueaty:
                a = np.double(image)
                b = a + 15
                image = np.uint8(b)
            
        try:
            transfer = color_transfer(affect, image)
            image=transfer
        except:
            pass
        cv2.imshow("color",image)
    cv2.imshow("color",image)
    key = cv2.waitKey(1)
    if key== ord("0"):
        affect=None
    if key== ord("a"):
        affect,l=nex(l=l,step='f')
    if key== ord("d"):
        
        affect,l=nex(l=l,step='d')
    if key== ord("b"):
        if bueaty:
            bueaty=False
        else:
            bueaty=True
    if key == 27:
        x=False




