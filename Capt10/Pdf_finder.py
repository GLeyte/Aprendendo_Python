import os, shutil
from pathlib import Path

dataPath = Path('C:/Users/Gabriel/Desktop/Graduation/Semestre6/Transcal')
dataTo = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/Capt10/PDFs')

for filename in dataTo.glob('*'):
    os.unlink(filename)
    # print(filename)

for folderName, subfolders, filenames in os.walk(dataPath):
    for filename in filenames:
        if filename.endswith('.pdf'):
            # print('FILE INSIDE ' + folderName + ': '+ filename)
            shutil.copy(dataPath/filename,dataTo)