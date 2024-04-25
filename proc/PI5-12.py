# Imagem de resolucao 500x300 com valores de BGR aleatorios entre 0 255 para cada vez que for criada

import cv2
import numpy as np
from random import randint

img = np.zeros((300, 400, 3), dtype=np.uint8)
for lin in img:
    cor = randint(0,255), randint(0,255), randint(0,255)
    for px in lin:
        px[:] = cor
    cv2.imshow("Bagre", img)
cv2.waitKey(0)
