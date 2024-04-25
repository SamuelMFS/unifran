# Dividir a imagem do carro em 12 partes iguais (3 linhas x 4 colunas)
# e  reposicionar cada uma das partes em lugares aleatorios sempre que
# o programa for executado.

import cv2
from skimage import io
import numpy as np
import random

img = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

altura, largura = img.shape[:2]
altura_parte = altura // 3
largura_parte = largura // 4

partes = []
for i in range(3):
    for j in range(4):
        parte = img[altura_parte * i: altura_parte * (i + 1), largura_parte * j: largura_parte * (j + 1)]
        partes.append(parte)

random.shuffle(partes)

imagem_embaralhada = np.zeros(img.shape, dtype=np.uint8)

idx = 0
for i in range(3):
    for j in range(4):
        imagem_embaralhada[altura_parte * i: altura_parte * (i + 1), largura_parte * j: largura_parte * (j + 1)] = partes[idx]
        idx += 1

cv2.imshow("titulo qlqr", imagem_embaralhada)
cv2.waitKey(0)
