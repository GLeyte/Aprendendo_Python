import requests
from pathlib import Path

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/Capt12')

res.raise_for_status()

file = open(dataPath/"Romeu.txt",'wb')

for chunk in res.iter_content(0):
        file.write(chunk)

file.close()