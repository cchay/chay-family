import  time
import random
import sys

print("Welcome to world Championships.")
time.sleep(1)
p1 = input("What is your name?")

p2  = input("Player2 what is your name?")

print(p1,"will fight",p2,".!")
           
###### Battle ############################

p1Health = random.randint( 50,100 )
p2Health = random.randint( 50,100 )

while p1Health >= 0 and p2Health >= 0:
   time.sleep(0.5)
   print( p1,'\'s health: ',p1Health )
   print( p2,'\'s health: ',p2Health )
   p1Damage = random.randint( 1, 10 )
   p2Damage = random.randint( 1, 10 )
   

   if random.randint(1, 2) == 1:
       p2Health = p2Health - p1Damage
       print( p1,'has hit',p2,' for ',p1Damage)
   else:
      print('You missed!')

   if random.randint(1, 2) == 1:
       p1Health = p1Health - p2Damage
       print( p2,'has hit',p1,' for ',p2Damage)
   else:
      print('He missed!')

else:
   if p1Health and p2Health < 1:
      print(p1,'and the ',p2,'Knocked out')
      sys.exit()
   elif p1Health < 1:
      print(p1,'You got defeated by ',p2)
      sys.exit()
   elif p2Health < 1:
       print('The ',p2,' had Knocked out!!')


