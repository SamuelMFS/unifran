# Separacao dos canais de cor (apenas uma cor retida e as demais em nivel 0)

import cv2
from skimage import io

img = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # Converte de RGB para BGR
rv, rh = img.shape[:2]
# Mostra a imagem em uma janela criada com nome "Normal"
cv2.imshow("Normal", img)
cv2.moveWindow("Normal", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()

b = img.copy()
b[:,:,1] = b[:,:,2] = 0 # seleciona todas as colunas e linhas insere preto (0) no G b[1] e no R b[2] e deixa o B b[0] como estava
cv2.imshow("Normal", b)
cv2.moveWindow("Normal", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()

g = img.copy()
g[:,:,0] = g[:,:,2] = 0 # seleciona todas as colunas e linhas insere preto (0) no B b[0] e no R b[2] e deixa o G b[1] como estava
cv2.imshow("Normal", g)
cv2.moveWindow("Normal", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()

r = img.copy()
r[:,:,0] = r[:,:,1] = 0 # seleciona todas as colunas e linhas insere preto (0) no B b[0] e no G b[1] e deixa o R b[2] como estava
cv2.imshow("Normal", r)
cv2.moveWindow("Normal", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()
