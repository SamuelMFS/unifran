import cv2
from skimage import io

# Carrega a imagem
imagem = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)

# Exibe a imagem em uma janela
cv2.imshow('Imagem', imagem)

# Aguarda que uma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas abertas
cv2.destroyAllWindows()
