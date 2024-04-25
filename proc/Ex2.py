import cv2
from skimage import io
import numpy as np
from google.colab.patches import cv2_imshow

img = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

altura, largura = img.shape[:2]
altura_parte = altura // 2
largura_parte = largura // 2

img[altura_parte: altura_parte * 2, largura_parte: largura_parte * 2, 0] = img[altura_parte: altura_parte * 2, largura_parte: largura_parte * 2, 1] = 0
img[: altura_parte, largura_parte: , 1] = img[: altura_parte, largura_parte:, 2] = 0
img[altura_parte: altura_parte * 2, :largura_parte, 0] = img[altura_parte: altura_parte * 2, :largura_parte, 2] = 0

cv2_imshow(img)
