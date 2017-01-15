##with the help of my brothers###
import random
import time
import sys
##teams
country1 = input('Team1 what is your Country Name?')
time.sleep(1)

country2 = input('Team2 what is your Country Name?')
time.sleep(1)
############ Number of armies per team ############
armyA = int(input("Team1 how many men do you have?"))
time.sleep(1)

armyB = int(input("Team2 how many men do you have?"))
time.sleep(1)

## prints the name of the country,and how many armies there here ##
print('country1:',country1)
print('armyA:',armyA)
time.sleep(1)
print('country2:',country2)
print('armyB:',armyB)

###### Battle ############################

while armyA > 0 and armyB > 0:
   time.sleep(0.5)
   print( country1,'\'s men: ',armyA )
   print( country2,'\'s men: ',armyB )
   country1Damage = random.randint( 1, 6 )
   country2Damage = random.randint( 1, 6 )
   

   if random.randint(1, 2) == 1:
       armyB = armyB - country1Damage
       print( country1,'has destroyed',country2,' for ', country1Damage)
   else:
      print('You missed!')

   if random.randint(1, 2) == 1:
       armyA = armyA -  country2Damage
       print( country2,'destroyed',country2,' for ', country2Damage)
   else:
      print('He missed!')
################die or live#########################
else:
   if armyA  and armyB < 1:
      print(country1,'and the ',country2,'Knocked out')
      sys.exit()
   elif armyA < 1:
      print(country1,'You got defeated by ',country2)
      sys.exit()
   elif armyB < 1:
       print('The ',countryB,' had Knocked out!!')
