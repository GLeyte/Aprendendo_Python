from pathlib import Path
import random
import numpy as np
dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/text_generate_change')

data_num = random.randint(1000, 2000)

file = open(dataPath/'original.txt','w')

mean = 50
sigma = 1

nums = list(np.random.normal(mean, sigma, data_num))

for num in nums:

    file.write(f'{num:.4f}\n')

file.close()
