"""
Created on Wed Jun 23 18:09:42 2021
@author: odomi
"""
#from imutils.video import VideoStream
#omariimport imutils
import time
import cv2
#import sys
import os

#captura = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)
outputDir = os.path.join("C:/discoF/proyectos/fotos/fotos/fotosP/s26")

#outputDir = os.path.join(args["output"]
count = 0
# initialize the video stream and allow the cammera sensor to warmup
nombre = input("teclea nombre")
print("[INFO] starting video stream...")
listo1 = input("listo")
#--------------------------------------------------
while (cap.isOpened()):
    ret, imagen = cap.read()
    #if ret == True:
      #  cv2.imshow('video', imagen)

        #salida.write(imagen)
#-----------------------------------------------

    if count >= 100:
        cap.release()
        break;
# grab the frame from the video stream and resize it to have a
# maximum width of 400 pixels
    print("conta", count)
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('video', frame)
    #frame = imutils.resize(frame, width=400)
    frame = cv2.resize(frame,(400,300),interpolation=cv2.INTER_CUBIC)
# show the output frame
    #cv2.imshow("Frame", frame)
    #key = cv2.waitKey(1) & 0xFF
    #filename = "{}.jpg".format(str(count).zfill(4))
    filename = (nombre+str(count)+".jpg")
    cv2.imwrite(os.path.join(outputDir, filename), frame)
    count = count+1
# do a bit of cleanup
cap.release()
#salida.release()
print("apagado")
cv2.destroyAllWindows
