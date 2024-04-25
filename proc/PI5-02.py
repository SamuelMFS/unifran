# Converte a imagem de RGB para BGR para que possa ser usada no opencv

import cv2
from skimage import io

img = io.imread('https://pazeamor.pt/wp-content/uploads/2019/10/praia-da-legua-2.jpg')
for lin in img:
        for px in lin: # px [e o pixel em RGB (px[0], px[1], px[2])]
            px[0], px[2] = px[2], px[0]
rv, rh = img.shape[:2]

# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # outra maneira de fazer, usando a funcao do opencv
#
# img = img[:,:,::-1] # outra maneira de fazer, invertendo diretamento os valores da matriz

img = cv2.resize(img, (int(rh * 0.5), int(rv * 0.5)))
cv2.imshow('Imagem', img)

cv2.moveWindow("Imagem", 2200, 20)

cv2.waitKey(0)

cv2.destroyAllWindows()
