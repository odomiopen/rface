#programa para detectar y reconocer rostros para su ingreso a un laboratorio LBPH
import time
import cv2
from time import sleep                                                                                                                                                                                                                                                                                                                                                                                                                                                       
import os  # Importa el módulo os
from picamera2 import Picamera2
#from picamera2.encoders import H264Encoder
import numpy as np


face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("/home/rf/Documentos/xmlrostros/modeloLBPHFace504All.xml")
faceClasificado = cv2.CascadeClassifier('/home/rf/Documentos/xmls/haarcascade_frontalface_default.xml')

# initialize the video stream and allow the cammera sensor to warmup
picam2 = Picamera2()
picam2.start_preview()
#vs = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
time.sleep(1.0)
picam2.preview_configuration.main.size = (400,300)

while True:
    picam2.start()
    frame = picam2.capture_array()
#Dibuja el rectángulo dentro de la imagen con ciertas coordenadas
    cv2.rectangle(frame, (100, 10), (300, 290), (255, 0, 255), 2)
    #cv2.imshow("Frame", frame)
    img_recortada= frame[10:290, 100:300]
    #cv2.imshow("FrameR", img_recortada)
    gray = cv2.cvtColor(img_recortada,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gris", gray)
#La función detectMultiScale se utiliza para detectar las caras. Se necesitan 3 argumentos  
    faces = faceClasificado.detectMultiScale(gray, 1.2, 4)
    #print("detec",faces)
    aux_frame = gray.copy()
    for(x, y, w, h) in  faces:
        rostro = aux_frame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro,(200,280),interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)
        cv2.putText(frame, '{}'.format(result), (x, y-5), 1, 1.3, (0, 255, 0), 1,cv2.LINE_AA)

        #print('rostro', rostro)
        if result[1] < 70:
            cv2.putText(frame, '{}'.format(rostro[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1,cv2.LINE_AA)
#Dibuja el rectángulo alrededor de cada cara
            cv2.rectangle(frame,(x+100,y+10), (x+100+w,y+10+h), (0,255,0),1,cv2.LINE_AA)
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)
            cv2.putText(frame, 'Positivo', (x, y-20), 2, 0.8, (0, 0, 255), 1,cv2.LINE_AA)
                           
        else:
            cv2.putText(frame, 'Desconocido', (x, y-20), 2, 0.8, (0, 0, 255), 1,cv2.LINE_AA)
            cv2.rectangle(frame, (x+100,y+10), (x+100+w,y+10+h), (0,0,255),2)
#cv2.imshow("gris", gray)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        vs.stop()
        break;       
cv2.destroyAllWindows()


