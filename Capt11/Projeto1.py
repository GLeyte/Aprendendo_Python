import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

change = {'heads':1,'tails':0}

logging.debug(change)

guess = ''
while guess not in [0,1]:
    print('Guess the coin toss! Enter heads or tails:')

    toss = random.randint(0, 1) # 0 is tails, 1 is heads

    logging.debug(f'toss:{toss}')

    guess = change[input()]
    

    logging.debug(f'guess:{guess}; toss:{toss}')

    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = change[input()]
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')