# colocar a imagem em escala de cinza (grayscale)

import cv2
from skimage import io
import numpy as np

img = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Metodo 1: usando a funcao cv2.cvtColor
met1 = img.copy()
met1 = cv2.cvtColor(met1, cv2.COLOR_BGR2GRAY)

# Metodo 2: fazendo media aritimetica dos canais de cada pixel
met2 = img.copy()
rv, rh = met2.shape[:2]
for i in range(rv):
    for j in range(rh):
        met2[i, j] = np.average(met2[i, j])  # ou sum(img[i, j]) // 3

# Metodo 3: percorrendo as linhas e os pixels das linhas
met3 = img.copy()
for lin in met3:
    for px in lin: # px eh o pixel em RGB (px[0], px[1] e px[2])
        px[:] = np.average(px) # insere o valor da media para BGR diretamente
 
# Metodo 4: cirando uma nova matirz 2D com apenas um valor para cada pixel
rv, rh = img.shape[:2]
met4 = np.zeros((rv, rh), dtype=np.uint8)
for i in range(rv):
    for j in range(rh):
        met4[i, j] = np.average(img[i, j])

# Metodo 5: usando equacao (RGB - Cionza):
met5 = img.copy()
for lin in met5:
    for px in lin:
        px[:] = 0.299 * px[0] + 0.587 * px[1] + 0.114 * px[2]

met1 = cv2.resize(met1, (rv, rh))
met2 = cv2.resize(met2, (rv, rh))

concatenadas12 = np.hstack((met1, met2))
# concatenadas34 = np.hstack((met3, met4))
# concatenadas1234 = np.hstack((concatenadas12, concatenadas34))
# concatenadas12345 = np.hstack(concatenadas1234, met5)

cv2.imshow("Bagre", concatenadas12)
cv2.moveWindow("Bagre", 2200, 20)

cv2.waitKey(0)

cv2.destroyAllWindows()
