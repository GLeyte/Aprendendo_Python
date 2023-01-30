from pathlib import Path
import os

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/FileStudy/textos')

original = open(dataPath/'original.txt')

texto_original = original.read()

palavras = texto_original.split()

trocas = ['may']

for i in range(len(palavras)):

    if  palavras[i].lower() == trocas[0]:
        antiga = list(palavras[i])
        antiga = list('SAPATO') + antiga[9:]
        palavras[i] =''.join(antiga)
    else:
        palavras[i]='-'

texto = ' '.join(palavras)

original.close()

novo = original = open(dataPath/'novo.txt','w')

novo.write(texto)

novo.close()