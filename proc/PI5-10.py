# converter imagem para hsv e modificar o valor de saturacao

import cv2
from skimage import io
import numpy as np

img = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow("Bagre", img)
cv2.waitKey(0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img)
s = np.float64(s)
s *= 0.5
s = np.clip(s, 0, 255)
s = np.uint8(s)
img = cv2.merge([h,s,v])
img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.imshow("Oto bagre", img)
cv2.waitKey(0)
