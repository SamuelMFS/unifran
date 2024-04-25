import cv2
from skimage import io
import numpy as np

img = np.zeros((300,300, 3), dtype=np.uint8)

cv2.imshow("A", img)
cv2.waitKey(0)

# positivo conta do superior esquerdo(1,1), negativo conta do inferior direito(-1, -1)
img[:5, :5] = [0, 0, 255]
cv2.imshow("A", img)
cv2.waitKey(0)
img[:, :] = [0, 0, 0]

img[-1:-20, -1:-20] = [0, 0, 255]
cv2.imshow("A", img)
cv2.waitKey(0)
img[:, :] = [0, 0, 0]


img[30:270, 30:270] = [255, 0, 0] # ou [30:-30] daria o mesmo resultado
img[60:240, 60:240] = [0, 255, 0] # ou [60:-60] daria o mesmo resultado
img[90:210, 90:210] = [0, 0, 255] # ou [90:-90] daria o mesmo resultado
img[120:180, 120:180] = [255, 255, 255]  # ou [120:-120] daria o mesmo resultado
cv2.imshow("A", img)
cv2.waitKey(0)
