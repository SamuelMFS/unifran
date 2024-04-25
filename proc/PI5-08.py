# alterando contraste e brilho da imagem

import cv2
from skimage import io
import numpy as np
import tkinter as tk
from tkinter import simpledialog

def brilho_contraste():
    contraste = simpledialog.askinteger("Contraste", "Digite o valor de contraste (1-100):", initialvalue=50)
    brilho = simpledialog.askinteger("Brilho", "Digite o valor de brilho (1-100):", initialvalue=50)
    
    imgcp = img.copy()
    imgcp = imgcp * ((2 * contraste - 50) / 50) + (5 * (brilho - 50))
    imgcp[imgcp > 255] = 255
    imgcp[imgcp < 0] = 0
    imgcp = np.uint8(imgcp)
    
    cv2.imshow('Imagem com Brilho e Contraste Ajustados', imgcp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Carregar a imagem
img = io.imread('https://cdn.salaodocarro.com.br/_upload/content/2018/08/31/tesla-apresentar-novo-carro-proximos-dias_album.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Criar uma janela tkinter
root = tk.Tk()
root.title("Ajuste de Brilho e Contraste")

# Criar um botão
button = tk.Button(root, text="Ajustar Brilho e Contraste", command=brilho_contraste)
button.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()
