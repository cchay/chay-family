import random

class FantasyCharacter:
   def __init__( self, status ):
      self.name = input( 'What is your name?\n' )
      self.gender = input( 'What is your gender?\n' )
      self.race = input( 'What is your race?( Troll, giant, human e.g. )\n' )
      self.age = input( 'How old are you?\n' )
      self.desc = input( 'Describe yourself:\n' )
      self.life = random.randint( 10, 50 )
      self.gold = random.randint( 10, 50 )
      self.status = status
      self.weapon = input( 'What is your weapon?\n' )
      self.clothes = "cotton cloak"

class Weakling(FantasyCharacter):
   def __init__( self, clothes ):
      FantasyCharacter.__init__(self, status())
      self.clothes = clothes
      self.gold = random.randint( 5, 40 )
      self.life = random.randint( 5, 40 )

def status():
   status = ["noble","poor", "not so rich", "not that poor","rich"]
   return status[random.randint(0, 4)]

clothes = "coarse linen cloak"
char = []

print( 'Welcome to the world of survival!!' )
print( 'Character 1:' )
char1 = FantasyCharacter( status() )
char.append(char1)

print( '\nCharacter 2:' )
char2 = FantasyCharacter( status() )
char.append(char2)

print( '\nCharacter 3:' )
char3 = Weakling( clothes )
char.append(char3)

for i in range(len(char)):
   print( '''
Name: {0}
Gender: {1}
Age: {2}
Race: {3}
Life: {4}
Status: {5}
Gold: {6}
Clothes: {7}
Weapon: {8}

''' .format( char[i].name, char[i].gender, char[i].age, char[i].race, char[i].life, char[i].status, char[i].gold, char[i].clothes, char[i].weapon) )
