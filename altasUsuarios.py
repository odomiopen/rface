#programa para dar de alta a los usuarios del sistema RF
import time
import cv2
from time import sleep                                                                                                                                                                                                                                                                                                                                                                                                                                                       
import os  
from picamera2 import Picamera2
import numpy as np

nombre = input("teclea nombre")
print("[INFO] starting video stream...")
listo1 = input("listo")

picam2 = Picamera2()
picam2.start_preview()
outputDir = os.path.join("/home/rf/Documentos/fotos/fotosP/s24")

count = 0

picam2.preview_configuration.main.size = (400,300)
time.sleep(1.0)

while count < 100:
    # Captura un fotograma
    picam2.start()
    frame = picam2.capture_array()
    print(count)#cv2.imshow("foto", frame)
    filename = (nombre+str(count)+".jpg")
    cv2.imwrite(os.path.join(outputDir, filename),frame)  # Utiliza os.path.join para unir rutas de directorios
    count += 1
    sleep(0.1)  # Pausa de 0.1 segundos entre cada captura

# Detener la grabación y la vista previa después de capturar las imágenes
picam2.stop_recording()
picam2.stop_preview()