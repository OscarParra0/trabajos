#Librería
import cv2
import numpy as np


#Tamaño de la ventana (pixeles)
bgr=np.zeros((300,300,3),dtype=np.uint8)
#color de la ventana
bgr[:,:,:]=(0,255,255)
#Mostrar ventana
cv2.imshow('BGR',bgr)

#Destruir Ventana
cv2.waitKey(0)
cv2.destroyAllWindows()