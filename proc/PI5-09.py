# alteracao dos valores com matriz numpy

import numpy as np

mat = np.zeros((5, 5), dtype=np.uint8)
mat[:,:] = 300 # overflow (valor retorna ao inicio - zero)
print(mat, mat.dtype)

mat = np.zeros((5, 5), dtype=np.uint8)
mat = mat + 300 # aqui a matriz tem seu tipo alterado para 16 bits
print(mat, mat.dtype)
