class Person:
   def __init__(self, name, age, race, gender):
      self.name = name
      self.age = age
      self.gender = gender
      self.race = race

   def __str__(self):
      return '''
              Name:    {}
              Age:     {}
              Gender:  {}
              Race:    {}

''' .format( self.name, self.age, self.race, self.gender )

p1 = Person( 'Melvin Marigun', 15, 'male', 'unknown' )
p2 = Person( 'Brian Faray', 25, 'male', 'White' )

print(str(p1) + '\n' + str(p2))
