import requests
from pathlib import Path

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/Capt12')

file = open(dataPath/"Romeu.txt",'w')

file.write(res.text[:100])

file.close()