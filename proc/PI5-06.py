# criando cor em cv2
import cv2
from skimage import io
import numpy as np

img = np.zeros((50, 50), dtype=np.uint8)
cv2.imshow("bagre", img)
cv2.waitKey(0)
img[:, :] = 128
cv2.imshow("bagre", img)
cv2.waitKey(0)
img[:, :] = 255
cv2.imshow("bagre", img)
cv2.waitKey(0)
