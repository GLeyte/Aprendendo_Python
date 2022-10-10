import random
from pathlib import Path
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


dataPath = Path('C:/Users/Gabriel/Desktop/Códigos/Git/Aprendendo_Python/FileStudy/quizzes')


for quizNum in range(3):

  quizFile = open(dataPath / f'quiz{quizNum+1}.txt', 'w')
  respostaFile = open(dataPath / f'resposta{quizNum+1}.txt', 'w')

  quizFile.write("Nome:\nData:   /   /   \n")
  quizFile.write(f'Estados e capiais Quiz (Tipo {quizNum + 1})')
  quizFile.write('\n\n')

  estados = list(capitals.keys())

  random.shuffle(estados)

  # pergunta

  for questionNum in range(len(capitals)):

    resposta = capitals[estados[questionNum]]
    erradas = list(capitals.values())
    erradas.remove(resposta)
    erradas = random.sample(erradas,3)
    options = [resposta] + erradas
    random.shuffle(options)

    quizFile.write(f'Questao {questionNum+1}. Qual a capital de {estados[questionNum]}?\n')

    for i in range(4):
      quizFile.write(f"       {'ABCD'[i]}.{options[i]}\n")
    quizFile.write('\n')

    respostaFile.write(f"{questionNum + 1}.{'ABCD'[options.index(resposta)]}\n")

  quizFile.close()
  respostaFile.close()
