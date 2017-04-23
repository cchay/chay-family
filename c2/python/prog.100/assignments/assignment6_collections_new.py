# Christopher Chay
# Assignment 6
# 2016.6.23
# Grade: ___47.5%___

import sys

SpiderMan = {'Secret Identity': "Peter Parker",
             'Age': 20,
             'Powers': "Wall crawling, super strength, agility, web"}

CapA= {'Secret Identity': "Steve Rogers",
       'Age': 18,
       'Powers': "Super strength, super-high endurance"}

SuperMan = {'Secret Identity': 'Clark Kent',
            'Age': 32,
            'Powers': "Super strength, Flight, Laser-vision, Heat-Vision, Icy-Breath"}

hero_attributes = ['Secret Identity', 'Age', 'Powers']

super_hero_list = {'Spider Man': ('Spider Man', SpiderMan),
                   'Captain America': ('Captain America', CapA),
                   'Super Man': ('Super Man', SuperMan)}



# Extra assignments

print('Super Heroes:')
for super_hero in super_hero_list:
   print(str(super_hero), '\t', end = "" )
   
print('\n\n\nSuper Hero Attributes:\n')
for super_hero in hero_attributes:
   print(super_hero)


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


# Q: What are Collections?
# A: They are lists and dictionaries which allow you to have mulitple different
#    values stored in a single variable so you can work with them collectively.
#
# Q: What does that mean?
# A: It means you can many different values stord ina variable.
#
# Q: How do you work with collections?
# A: You use it the same way you use lists and dictionaries
#
# Q: Why do you use collections?
# A: I would use them to store multiple different values in a single variable

