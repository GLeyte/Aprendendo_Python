import re,os
from pathlib import Path

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/Capt10/Datas')
dataPath_new = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/Capt10/Datas_new')

dataEUA = re.compile(r'''
    (\d+)/
    (\d+)/
    (\d+)
''', re.VERBOSE)


for fileAqrv in os.listdir(dataPath):
    file = open(dataPath / fileAqrv)
    file_new = open(dataPath_new / ('new'+fileAqrv),'w')

    datas = file.read().split()

    file.close()

    for data in datas:
        mo = dataEUA.search(data)
        
        if mo==None:
            continue

        mes = mo.group(1)
        dia = mo.group(2)
        ano = mo.group(3)

        data_new = dia+'/'+mes+'/'+ano

        tam = len(data)
        space = (50-tam)*' '

        file_new.write(f'{data}{space}{data_new}\n')
