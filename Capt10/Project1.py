import re,os
from pathlib import Path

dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/Capt10/datas')

dataEUA = re.compile(r'''
    (\d+)/
    (\d+)/
    (\d+)

''', re.VERBOSE)


print(os.listdir(dataPath))

# for folderName, subfolders, filenames in os.walk(dataPath):
#     print('The current folder is ' + folderName)

#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': '+ filename)

#     print('')