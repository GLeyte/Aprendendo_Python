from pathlib import Path
import os

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/FileStudy/textos')

original = open(dataPath/'original.txt')

texto_original = original.read()

palavras = texto_original.split(" ")

trocas = ['ADJECTIVE','NOUN','ADVERB','VERB']

for i in range(len(palavras)):

    if  trocas[0] in palavras[i]:
        print('Enter an adjective:')
        troca = list(input())
        antiga = list(palavras[i])
        antiga = troca + antiga[9:]
        palavras[i] =''.join(antiga)
    elif trocas[1] in palavras[i]:
        print('Enter an noun:')
        troca = list(input())
        antiga = list(palavras[i])
        antiga = troca + antiga[4:]
        palavras[i] =''.join(antiga)
    elif trocas[2] in palavras[i]:
        print('Enter an adverb:')
        troca = list(input())
        antiga = list(palavras[i])
        antiga = troca + antiga[6:]
        palavras[i] =''.join(antiga)
    elif trocas[3] in palavras[i]:
        print('Enter an verb:')
        troca = list(input())
        antiga = list(palavras[i])
        antiga = troca + antiga[4:]
        palavras[i] =''.join(antiga)

texto = ' '.join(palavras)

original.close()

novo = original = open(dataPath/'novo.txt','w')

novo.write(texto)

novo.close()
