from pathlib import Path
import os
# import matplotlib.pyplot as plt
# import re

# num = re.compile(r'-?\d\.\d{7}e.\d{2}')

# dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python//FileStudy/Dados_Sem_Falha')

# arquives=list(dataPath.glob('*'))

# tempo = num.findall(arquives[0].read_text())
# x = num.findall(arquives[1].read_text())
# y = num.findall(arquives[2].read_text())


# for i in range(len(tempo)):
#     tempo[i] = float(tempo[i])
#     x[i] = float(x[i])
#     y[i] = float(y[i])

# plt.plot(tempo, x)
# plt.show()

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python//FileStudy')

'''
LER

file = open(dataPath / 'file.txt')

file.close()

print(file.read())
'''

'''
ESCREVER

file = open(dataPath / 'file.txt','w')    #Escreve por cima do arquivo

file.close()

file = open(dataPath / 'file.txt','a')    #Escreve na linha final do texto (soma texto)

file.close()

file = open(dataPath / 'file.txt')

print(file.read())
'''

import shelve



'''shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))'''

import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)    
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()