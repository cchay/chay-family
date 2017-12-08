import random, sys, time

creatures = ["Giant",
             "Snake", 
             "Bandit", 
             "Mercenary", 
             "Rogue Knight", 
             "Bear", 
             "King Crab"]

congradulations = ["Awesome",
                   "Great",
                   "Cool beans",
                   "Congradulations",
                   "Sweet",
                   "Nice",]

foods = ["Pork Chop",
         "Bacon Slice",
         "Baked Potato",
         "Bread Loaf",
         "Steak",
         "Fruit",]


mapsize = (10, 10)

class player():
   def __init__(self):
      self.name = "Jean"
      self.gold = 10
      self.status = "alive"
      self.hp = 10
      
      ## Jean's location on the map
      ## map size is 3X3
      self.xcoor = 0
      self.ycoor = 0
   
   def death(self):
      if self.hp <= 0:
         self.status = "dead"
     
   
   def check_wall_ew(self, coor):
      if self.xcoor == mapsize[0]:
         if coor == -1:
            self.xcoor += coor
            event()
         else:
            print('You cannot go there!')
         
      elif self.xcoor == 0-int(mapsize[0]):
         if coor == 1:
            self.xcoor += coor
            event()
         else:
            print('You cannot go there!')
      else:
         self.xcoor += coor
         event()


   def check_wall_ns(self, coor):
      if self.ycoor == mapsize[1]:
         if coor == -1:
            self.ycoor += coor
            event()
         else:
            print('You cannot go there!')
         
      elif self.ycoor == 0-int(mapsize[1]):
         if coor == 1:
            self.ycoor += coor
            event()
         else:
            print('You cannot go there!')

      else:
         self.ycoor += coor
         event()
         
   
def event():
   chance = random.randint(1, 100)
   '''20% gold, 
      20% food loot
      20% Monster Attack
      40% nothing
      '''
   if chance <= 20:
      gold = random.randint(1, 20)
      print('{}! You have found {} gold!' .format(random.choice(congradulations), gold))
   
   elif chance >= 21 and chance <= 40:
      print('{}! You have found {}' .format(random.choice(congradulations), random.choice(foods)))
   
   elif chance >= 41 and chance <= 60:
      print('!!! A {} attacks you!!' .format(random.choice(creatures)))
      print('You lose 1 Hitpoint.')
      player.hp -= 1
      
      if player.hp <= 0:
         player.death()
         print('You die!')
   
   elif chance >= 61 and chance <= 100:
      print('You found nothing. The room is empty and bare.')
   

   
player = player()

while player.status == "alive":
   print('\n'*25)
   print('Hitpoints: {}' .format(player.hp))
   print('Mapsize: {}x{}' .format(mapsize[0], mapsize[1]))
   print('Coordinates: X: {}, Y: {}' .format(player.xcoor, player.ycoor))
   direction = input('In what direction will you go? Options: (n / s / e / w)')
   
   if direction == "n":
      player.check_wall_ns(1)
   
   elif direction == "s":
      player.check_wall_ns(-1)
   
   elif direction == "e":
      player.check_wall_ew(1)
   
   elif direction == "w":
      player.check_wall_ew(-1)
   
   elif direction == "q":
      sys.exit()
   
   else:
      pass
   

   









