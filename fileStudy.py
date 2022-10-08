from pathlib import Path
import os
from tkinter import X

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/Dados_Sem_Falha')

arquives=list(dataPath.glob('*'))

tempo = arquives[0].read_text().split('   ')
x = arquives[1].read_text().split('   ')
y = arquives[2].read_text().split('   ')

for i in range(len(tempo)):
    tempo[i] = float(tempo[i])
    x[i] = float(x[i])
    y[i] = float(y[i])

print(tempo[0:10])
print(arquives[1])