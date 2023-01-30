from pathlib import Path
dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/FileStudy')
file = open(dataPath/'file.txt')

print(file.read().split('\n'))