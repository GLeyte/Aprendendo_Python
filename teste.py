import pyinputplus as pyip
import sys

resposta = 'sim'

while resposta.lower() == 'sim':

    resposta = pyip.inputYesNo("teu ai\n", yesVal='sim', noVal='nao')

if resposta.lower() == 'nao':
    sys.exit