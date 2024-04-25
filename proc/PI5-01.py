import cv2
from skimage import io

# Carrega a imagem
imagem = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)

# Copia a Imagem
rv, rh = imagem.shape[:2]
q1 = imagem[:rv // 2, :rh // 2]
q2 = imagem[:rv // 2, rh // 2:]
q3 = imagem[rv // 2:, :rh // 2]
q4 = imagem[rv // 2:, rh // 2:]

# Exibe q1 em uma janela
cv2.imshow('Imagem', q1)
cv2.moveWindow("Imagem", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Exibe q2 em uma janela
cv2.imshow('Imagem', q2)
cv2.moveWindow("Imagem", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Exibe q3 em uma janela
cv2.imshow('Imagem', q3)
cv2.moveWindow("Imagem", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Exibe q4 em uma janela
cv2.imshow('Imagem', q4)
cv2.moveWindow("Imagem", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()
