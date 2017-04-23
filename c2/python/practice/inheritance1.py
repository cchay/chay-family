import random

class Person:
   def __init__(self, name):
      self.name = name
      self.brainz = random.randint( 1, 10 )
      self.strength = random.randint( 1, 10 )
      self.speed = random.randint( 1, 10 )

   def __str__(self):
      return self.name + '\nStrength: ' + str(self.strength) + '\nSpeed: ' + str(self.speed) + '\nBrainz:' + str(self. brainz)

boy1 = Person( input('name: ') )
boys = []
boys.append(boy1)

for i in boys:
   print( 'Boy', i )
   if i.brainz < 4:
      brainz = 'stupid'
   elif i.brainz < 7:
      brianz = 'average'
   else:
      brainz = 'smart'

   if i.speed < 4:
      speed = 'slow'
   elif i.speed < 7:
      speed = 'average'
   else:
      speed = 'fast'

   if i.strength < 4:
      strength = 'weak'
   elif i.speed < 7:
      strength = 'average'
   else:
      strength = 'strong'
   
   print( 'This kid is ', brainz + ',', strength + ' and ' + speed )










   
