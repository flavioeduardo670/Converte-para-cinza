from PIL import Image as img
import numpy as np
from matplotlib import pyplot as plt

# Encontra o caminho da imagem
filename = r"imagem.jpg"

# Abre a imagem e guarda na variável "IMAGEM", e depois salva na variável "matriz"
# um vetor tridimensional as informações de cada pixel da imagem
with img.open(filename) as IMAGEM:
    matriz = np.asarray(IMAGEM, dtype=np.float32)/255

# Mostra a imagem normal
IMAGEM.show()

print("Processando...")

# Cria três laços de repetição para acessar pixel a pixel da 
# imagem e alterar um por um, calculando a média dos valores RGB
# e depois atribuindo a mesma a cada um desses valores
# Exemplo: matriz[0][0] = (4, 8, 12)
# Média dos valores RGB: ( 4 + 8 + 12) / 3 = 8
# Atribui a cada um dos valores RGB: matriz[0][0] = (8, 8, 8)
for c in range(matriz.shape[0]):
    for d in range(matriz.shape[1]):
        l = []
        for e in range(3):
                l.append(matriz[c, d, e])
        media = (l[0] + l[1] + l[2]) / 3
        matriz[c, d, 0] = media
        matriz[c, d, 1] = media
        matriz[c, d, 2] = media

print("Imagem carregada")

# Carrega
plt.figure(figsize=(3, 3))
im = plt.imshow(matriz, aspect='auto')
plt.axis('off')
plt.show()



print("Finalizou")

