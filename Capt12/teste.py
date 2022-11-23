import requests
from pathlib import Path

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/Capt12')

res.raise_for_status()

file = open(dataPath/"Romeu.txt",'wb')

i=0

for chunk in res.iter_content(10):
        i+=1
        file.write(chunk)

        if i>10:
            break

file.close()