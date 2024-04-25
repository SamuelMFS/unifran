# Separa cada canal de cor em uma unica matriz

import cv2
from skimage import io

img = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
b, g, r = cv2.split(img)

cv2.imshow("B", b)
cv2.moveWindow("B", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("G", g)
cv2.moveWindow("G", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("R", r)
cv2.moveWindow("R", 2200, 20)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(b[0, 100:220])
print(g[0, 100:220])
print(r[0, 100:220])
