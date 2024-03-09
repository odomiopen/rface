#programa para generar el modelo de reconocimiento de rostros bajo LBPH
"""
Created on Tue Jun 22 23:11:41 2021
@author: odomi
"""
#importar librerias
import cv2
import os
import numpy as np

face_cascade = cv2.CascadeClassifier('/home/rf/Documentos/xmls/haarcascade_frontalface_default.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()


def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    
    if (len(faces) == 0):
        return None, None
    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    print(dirs)
    faces = []
    labels = []
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue;
        label = int(dir_name.replace("s", ""))
        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)
        for image_name in subject_images_names:
            if image_name.startswith("."):
                continue;
            
            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            face, rect = detect_face(image)
            
            if face is not None:
                faces.append(cv2.resize(face,(150,150)))
                labels.append(label)
    face_recognizer.train(faces, np.array(labels))
    face_recognizer.write("/home/rf/Documentos/xmlrostros/modeloLBPHFace504All.xml")
        
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
    return faces, labels

print("Preparando datos...")
faces, labels = prepare_training_data("/home/rf/Documentos/fotos/fotosP")
print("Datos preparados")
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))
print("Predicting images...")
