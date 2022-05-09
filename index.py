#Librería
import cv2
from cv2 import imshow
"""import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'"""

imgText="minions"
#Lectura de imagen
img= cv2.imread(imgText+'.jpg',250)
#Metodo para invetir el color de la imagen
img_neg = cv2.bitwise_not(img)
#Metodo para mostrar resultado de la imagen invertida
cv2.imshow('negative',img_neg)
#Metodo para mostrar resultado de la imagen original dada una escala de colores
imshow('Imagen Original',img)

cv2.waitKey(0)
cv2.destroyAllWindows()