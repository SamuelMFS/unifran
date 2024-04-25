import cv2
from skimage import io

imagem = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)

# Aplicar desfoque médio (blur)
imagem_desfocada = cv2.blur(imagem, (5, 5))  # Kernel de 5x5, você pode ajustar o tamanho conforme necessário

# Aplicar desfoque gaussiano (gaussian blur)
imagem_desfocada_gaussian = cv2.GaussianBlur(imagem, (5, 5), 0)  # Kernel de 5x5, você pode ajustar o tamanho conforme necessário

# Exibir as imagens resultantes
cv2.imshow('Imagem Desfocada', imagem_desfocada)
cv2.imshow('Imagem Desfocada Gaussiana', imagem_desfocada_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
