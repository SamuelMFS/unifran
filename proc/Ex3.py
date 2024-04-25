import cv2
from skimage import io
import numpy as np

img = io.imread('https://auniao.pb.gov.br/noticias/caderno_diversidade/cientistas-descobrem-medidas-mais-precisas-de-materia-escura-do-universo-1/universo.jpg/@@images/image.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)
b, g, r = cv2.split(img)

altura, largura = img.shape[:2]
largura_faixa = largura // 5
altura_faixa = altura // 5

contraste = 50
brilho = 50
for i in range(1, 5):
    faixa = img[altura_faixa * i: altura_faixa * (i + 1), :]
    faixa = faixa * (( 2 * contraste - 50) / 50) + (5 * (brilho - 50))
    faixa[faixa > 255] = 255
    faixa[faixa < 0] = 0
    contraste -= 10
    brilho += 20
    
    img[altura_faixa * i: altura_faixa * (i + 1), :] = faixa


#    np.clip(0, 255, faixa)
#    img_hsv[altura_faixa * i: altura_faixa * (i + 1), :, 1] = faixa.astype(np.uint8)
#
#    faixa = img_hsv[altura_faixa * i: altura_faixa * (i + 1), :, 2]
#    faixa -= 1
#    img_hsv[altura_faixa * i: altura_faixa * (i + 1), :, 2] = faixa

cv2.imshow("pa", img)
cv2.waitKey(0)


