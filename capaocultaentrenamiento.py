'''DocString'''
import os
from time import time
import cv2 as cv
import numpy as np


DATA_RUTA='./Data'
listaData=os.listdir(DATA_RUTA)

ids=[]
rostrosData=[]
id=0

tiempoInicial = time()

for fila in listaData:
    rutaCompleta= DATA_RUTA + '/' + fila
    print('Iniciando lectura')
    for archivo in os.listdir(rutaCompleta):
        
        print('Imagenes: ', fila + '/' + archivo)
        ids.append(id)
        rostrosData.append(cv.imread(rutaCompleta + '/' + archivo, 0))
        
    id=id+1
    tiempoFinalLectura = time()
    tiempoTotalLectura= tiempoFinalLectura - tiempoInicial
    print('Tiempo total de lectura: ', tiempoTotalLectura)

entrenamientoEigenFaceRecogneizer = cv.face.EigenFaceRecognizer_create()
print('Iniciando entrenamiento...espere')
entrenamientoEigenFaceRecogneizer.train(rostrosData, np.array(ids))
tiempoFinalEntrenamiento=time()
tiempoTotalEntrenamiento=tiempoFinalEntrenamiento-tiempoTotalLectura
print('Tiempo entrenamiento total: ', tiempoTotalEntrenamiento )
entrenamientoEigenFaceRecogneizer.write('EntrenamientoEigenFaceRecognizer.xml')
print('Entrenamiento concluido')