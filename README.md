# Reconocimiento facial (pruebas curso Udemy) #
Este código es del curso en Udemy "Python para no matematicos: De 0 hasta reconocimiento facial".

## Stack tecnológico ##
El código esta realizado en python con la libreria opencv y numpy (array).

https://github.com/opencv/opencv
https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html

## Código ##
El código está compuesto por 3 archivos:

- capaentrada.py
- capaocultaentrenamiento.py
- capasalidarecfacial.py

Además de disponer el archivo para que coja la cara frontalmente:

- haarcascade_frontalface_default.xml (opencv)

capaentrada.py
--
En este archivo busca mediante webcam o por selección de un archivo multimedia (en este caso video), haga imágenes de la persona que salga en el video o webcam y guardarla en una carpeta con el nombre que tu le pongas.

capaocultaentrenamiento.py
--
En este archivo recoge todas las imagenes que se han realizado en el código de capaentrada.py y las analiza para convertir un archivo llamado EntrenamentoEigenFaceRecognizer.xml donde está todo e analisis de las fotos.

capasalidarecfacial.py
--
En este archivo le indicas un video o mediante webcam, y mediante el archivo EntrenamientoEigenFaceRecognizer.xml creado anteriormente, intenta reconocer la cara de la persona en caso de estar en el archivo xml.

Si la encuentra sale el nombre de la carpeta y en caso contrario indica que no se ha encontrado.