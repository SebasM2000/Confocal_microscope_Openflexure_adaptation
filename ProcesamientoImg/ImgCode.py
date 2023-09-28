# Librerías
import cv2 as cv
import numpy as np
import os

os.environ['QT_QPA_PLATFORM'] = 'xcb'


#ruta_abs_img = os.path.dirname(os.path.abspath(__file__))
#rutaImg = os.path.join(ruta_abs_img, "ProcesamientoImg/IMGPrueba.jpeg")
rutaImg = "/home/ender3/Sebastian_Marin/ProcesamientoImg/IMGPrueba.jpg"

img = cv.imread(rutaImg)
img2 = cv.resize(img, (255, 255))

cv.imshow('P', img2)

cv.waitKey(0)
cv.destroyAllWindows()