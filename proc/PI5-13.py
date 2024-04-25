# embaralha a imagem em 16 partes de tamanho igual

import cv2
from skimage import io
import numpy as np
import random

img = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

altura, largura = img.shape[:2]

partes = []
altura_parte = altura // 3
largura_parte = largura // 4

for i in range(3):
    for j in range(4):
        parte = img[i * altura_parte: (i + 1) * altura_parte, j * largura_parte: (j + 1) * largura_parte]
        partes.append(parte)

random.shuffle(partes)

imagem_reorganizada = np.zeros(img.shape, dtype=np.uint8)

idx = 0
for i in range(3):
    for j in range(4):
        imagem_reorganizada[altura_parte * i: (altura_parte * i) + altura_parte, largura_parte * j: (largura_parte * j) + largura_parte] = partes[idx]
        idx += 1
    
cv2.imshow("bagre", imagem_reorganizada)
cv2.waitKey(0)
