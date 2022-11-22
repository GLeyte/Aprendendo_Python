from pathlib import Path
import random,string

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/Capt10/Datas')

data_num = random.randint(100, 200)

for i in range(10):

    file = open(dataPath / f'datas{i+1}.txt','w')

    for i in range(data_num):

        dia = random.randint(1, 31)
        mes = random.randint(1, 12)
        ano = random.randint(20, 22)

        if dia>28 and mes==2:
            dia = 28

        lixo1 = random.choice(string.ascii_letters)*random.randint(1, 5)
        lixo2 = random.choice(string.ascii_letters)*random.randint(1, 5)

        file.write(f'{lixo1}{mes:02d}/{dia:02d}/{ano}{lixo2}\n')

    file.close()
