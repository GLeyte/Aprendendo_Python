from pathlib import Path
import os

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/Dados_Sem_Falha')

print(list(dataPath.glob('?_original.txt')))