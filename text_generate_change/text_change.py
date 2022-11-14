from pathlib import Path
import random
import matplotlib.pyplot as plt
import numpy as np

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/text_generate_change')

file = open(dataPath/'original.txt')
file_new = open(dataPath/'novo.txt','w')

numeros = file.read().split()

for numero in numeros:
    novo = numero.replace('.',",")
    file_new.write(f'{numero}         {novo}\n')

file.close()
file_new.close()

numeros = [float(i) for i in numeros]

from text_generate import mean,sigma

count, bins, ignored = plt.hist(numeros, 30, rwidth=0.9, color='red', alpha=0.7, edgecolor='black',density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mean)**2 / (2 * sigma**2) ),linewidth=2, color='b')
plt.show()