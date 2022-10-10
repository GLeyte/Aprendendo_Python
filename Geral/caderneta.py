###################    LISTAS   ########################

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1:3]  # ['bat', 'rat']


spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]  
spam        #  ['cat', 'bat', 'elephant']


spam = ['cat', 'bat', 'rat', 'elephant']
'cat' in spam   # True


supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
        print('Index ' + str(index) + ' in supplies is: ' + item)

'''
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders
'''

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('heyas')    # 3


spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()               # spam = ['ants', 'badgers', 'cats', 'dogs', 'elephants']
spam.sort(reverse=True)   # spam = ['elephants', 'dogs', 'cats', 'badgers', 'ants']

spam.reverse()     # inverte

##################   DICIONÁRIO   ##################

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

'''
red
42
'''

for k in spam.keys():
    print(k)

'''
color
age
'''   

for i in spam.items():
    print(i)

'''
('color', 'red')
('age', 42)
'''  

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')    # 'I am bringing 2 cups.'
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')    # 'I am bringing 0 eggs.'


##################   STRING   ##################

name = 'Al'
age = 4000
print(f'My name is {name}. Next year I will be {age + 1}.')    # 'My name is Al. Next year I will be 4001.'

spam = 'Hello, world!'
spam = spam.upper()            # spam = 'HELLO, WORLD!'
spam = spam.lower()            # spam = 'hello, world!'

spam.isalpha()                 # Returns True if the string consists only of letters and isn’t blank
spam.isalnum()                 # Returns True if the string consists only of letters and numbers and is not blank
spam.isdecimal()               # Returns True if the string consists only of numeric characters and is not blank
spam.isspace()                 # Returns True if the string consists only of spaces, tabs, and newlines and is not blank
spam.istitle()                 # Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters


'Hello, world!'.startswith('Hello')         # True

' '.join(['My', 'name', 'is', 'Simon'])     # 'My name is Simon'

'MyABCnameABCisABCSimon'.split('ABC')       # ['My', 'name', 'is', 'Simon']

'rjust(), ljust(), and center()'            # Ajuste de texto