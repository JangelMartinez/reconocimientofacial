'''DocString'''
import os
import cv2 as cv
import imutils

MODELO='FotosElonMusk'
RUTA1='./Data/'
RUTA_COMPLETA = RUTA1+MODELO

if not os.path.exists(RUTA_COMPLETA):
    os.makedirs(RUTA_COMPLETA)

# Para capturar la webcam
#camara=cv.VideoCapture(0)
    
# Para capturar un video
camara=cv.VideoCapture('ElonMusk.mp4')
    

ruidos=cv.CascadeClassifier('./haarcascade_frontalface_default.xml')

id=0

while True:
    respuesta,captura=camara.read()
    if respuesta is False:
        break

    # Redimensiono la captura para no gastar más recursos de los necesarios
    captura=imutils.resize(captura, width=640)

    # Se convierte la captura a grises
    grises=cv.cvtColor(captura, cv.COLOR_BGR2GRAY)

    idcaputura=captura.copy()

    cara=ruidos.detectMultiScale(grises,1.3,5)

    for(x,y,e1,e2) in cara:
        cv.rectangle(captura,(x,y), (x+e1,y+e2), (255,0,0), 2)
        rostrocapturado=idcaputura[y:y+e2, x:x+e1]
        rostrocapturado=cv.resize(rostrocapturado, (160,160), interpolation=cv.INTER_CUBIC)
        cv.imwrite(RUTA_COMPLETA + '/image_{}.jpg'.format(id), rostrocapturado)
        id=id+1

    cv.imshow("Resultado rostro", captura)

    ## Cuando llega a 500 imágenes, el programa se para.
    if id==500:
        break

    ## Se puede salir del programa, pulsando la letra 's'
    if cv.waitKey(1) == ord('s'):
        break

camara.release()
cv.destroyAllWindows()