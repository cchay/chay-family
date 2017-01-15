# Christopher Chay
# Assignment 7
# 2016.3.31
# Grade: _____


## How to put all this into minimally three functions..........

## Input, output, and data structure.......

import sys
### data structure
SpiderMan = {'Secret Identity': "Peter Parker",
             'Age': 20,
             'Powers': "Wall crawling, super strength, agility, web"}

CapA= {'Secret Identity': "Steve Rogers",
       'Age': 18,
       'Powers': "Super strength, super-high endurance"}

SuperMan = {'Secret Identity': 'Clark Kent',
            'Age': 32,
            'Powers': "Super strength, Flight, Laser-vision, Heat-Vision, Icy-Breath"}

###
hero_attributes = ['Secret Identity', 'Age', 'Powers']

super_hero_list = {'Spider Man': ('Spider Man', SpiderMan),
                   'Captain America': ('Captain America', CapA),
                   'Super Man': ('Super Man', SuperMan)}



# Extra assignments
### output

print('Super Heroes:')
for super_hero in super_hero_list:
   print(str(super_hero), '\t', end = "" )
   
print('\n\n\nSuper Hero Attributes:\n')
for super_hero in hero_attributes:
   print(super_hero)

### input
while True:
   user_input = input('\nWhich attribute of the heroes would you like to see? or type \'exit\' to exit.')

   if user_input == "exit":
      sys.exit()

   for attribute in hero_attributes:
      if user_input == attribute:
         for super_hero in super_hero_list:
            print(str(super_hero) + ':', super_hero_list[super_hero][1][user_input], '\n' )
##         sys.exit()
   else:
      print('You typed something wrong.')




'''
def createSuper( x, y, z, a ):
   x, y, z, a = x, y, z, a
   return 'Superhero: ' + x + '\n' + \
            'Secret Identity: ' + y + '\n' + \
            'Age: ' + str(z) + '\n' + \
            'Powers: ' + a
   

super1 = createSuper( 'Spider Man', 'Peter Parker', 20, 'Wall crawling, super strength, agility, web' )
super2 = createSuper( 'Captain America', 'Steve Rogers', 18, 'Super strength, Super-high Endurance, Super-speed' )
super3 = createSuper( 'Super Man', 'Clark Kent', 32, 'Super strength, Flight, Laser-vision, Heat-Vision, Icy-Breath' )
print( str(super1) + '\n\n' + str(super2) + '\n\n' + str(super3) )
'''

      












