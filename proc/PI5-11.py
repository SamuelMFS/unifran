# converter imagem para hsv e modificar o valor da saturacao

import cv2
from skimage import io
import numpy as np

img = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

saturacao = float(input("Entra a saturacao: "))
imgcp = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(imgcp)
s = np.float64(s)
s *= saturacao / 10
s = np.clip(0, 255, s)
s = np.uint8(s)
imgcp = cv2.merge([h,s,v])
imgcp = cv2.cvtColor(imgcp, cv2.COLOR_HSV2BGR)
cv2.imshow("bagre", imgcp)
cv2.waitKey(0)
