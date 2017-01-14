'''
animal_sizes = {'large':  'X >= 8ft',
                'medium': '3ft <= X <= 7ft',
                'small':  'X < 3ft'}



panda =  {'size': 'medium',       'status': 'Endangered'}
tiger =  {'size': 'medium-large', 'status': 'Endangered'}
crane =  {'size': 'medium',       'status': 'Least Concern'}
monkey = {'size': 'medium',       'status': 'Endangered'}
viper =  {'size': 'medium',       'status': 'Not Evaluated'}
mantis = {'size': 'Tiny',         'status': 'Least Concern'}

animals = {'Panda': panda,
           'Tiger': tiger,
           'Crane': crane,
           'Monkey': monkey,
           'Viper':  viper,
           'Mantis': mantis}


for animal in animals:
   print(animal, ':', animals[animal])
'''



# Assignment 5

animal = input('Type the name of any animal:')
if animal == "cat":
   print ("Hello Puss-in-Boots.")
elif animal == "panda":
   print('Greetings Dragon Warrior')
else:
   print ("Hello "+ animal)

