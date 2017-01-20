import random, pickle

armour = { 'robe': {'name': 'robe', 'armour': 2, 'Buy': 35, 'Sell': 15, 'location': 'torso'},
           'T-shirt': {'name': 'T-shirt', 'armour': 5, 'Buy': 80, 'Sell': 40, 'location': 'torso'},
           'jacket': {'name': 'jacket', 'armour': 20, 'Buy': 500, 'Sell': 200, 'location': 'torso'},
           'vest': {'name': 'vest', 'armour': 10, 'Buy': 200, 'Sell': 90, 'location': 'torso'}
           }

pants = { 'boxers': {'name': 'boxers', 'armour': 1, 'Buy': 25, 'Sell': 10, 'location': 'legs'},
           'tunic': {'name': 'tunic', 'armour': 3, 'Buy': 65, 'Sell': 30, 'location': 'legs'},
           'leggings': {'name': 'leggings', 'armour': 17, 'Buy': 450, 'Sell': 180, 'location': 'legs'},
           'shorts': {'name': 'shorts', 'armour': 8, 'Buy': 175, 'Sell': 80, 'location': 'legs'}
           }

trinkets = {'necklace': {'armour': 10, 'Buy': 200, 'Sell': 90},
            'head band': {'armour': 10, 'Buy': 200, 'Sell': 90},
            'wrist band': {'armour': 10, 'Buy': 200, 'Sell': 90},
            'eye patch': {'armour': 10, 'Buy': 200, 'Sell': 90}}

profiles = {}

class player:
   def __init__(self):
      self.name = 'Drakin'

      self.hp = random.randint(50, 100)
      self.nrg = random.randint(50, 150)
      self.element = random.choice(['Water', 'Fire', 'Air', 'Earth'])

      self.gear = {'legs': {'name': 'empty', 'armour': 0}, 'torso': {'name': 'empty', 'armour': 0}}
      self.armour = 10
      
      self.exp = 0
      self.level = 1
      self.n_level = 100
      
      self.gold = 10

   def __str__(self):
      return '''{}:
   Level: {}; Exp: {}/{}
   Health: {}
   Armour: {}
   Money: {}@
   Equipped Gear:
      Torso: {}
      Legs:  {}''' .format(self.name, self.level, self.exp, self.n_level, self.hp, self.armour, self.gold, self.gear['torso']['name'], self.gear['legs']['name'])

   def getExp(self, exp):
      self.exp += exp
      print('{} won. +{} experience gained.' .format(self.name, exp))

   def levelUp(self):
      if self.exp >= self.n_level:
         self.exp = self.exp - self.n_level
         self.level += 1
         self.n_level *= 2
         print('You have gained a level!')

   def findGold(self, loot):
      self.gold += loot
      print('{} found {}@' .format(self.name, loot))

   def equipArmour(self, armor, location):
      if armor['location'] in self.gear:
         self.gear[location] = armor
         print('{} equipped!' .format(armor['name']))
         player().calcArmour()
      else:
         print('Location not clearly expressed!')

   def calcArmour(self):
      self.armour = self.gear['torso']['armour'] + self.gear['legs']['armour']


def battle(f1, f2): # Change later
   exp_gained = random.randint(10, 20)
   gold_found = random.randint(1,  20)
   f1.getExp(exp_gained)
   f1.findGold(gold_found)
   f1.levelUp()

Hero = player()
'''
for i in range(5):
   print(Hero)
   battle(Hero, 'Wolf')
   if random.randint(1, 10) == 1:
      exp_gained = random.randint(100, 500)
      print('You\'ve succesfully completed a quest.')
      print('  +{} experience gained.' .format(exp_gained))
      Hero.getExp(exp_gained)
      Hero.levelUp()
   input('Hit <ENTER> To Continue')

   #with????
'''


class Shop:
   def armourShop(self):
      print('Hey, I\'m Changdon. What can I do for ya? Here are my wares: ')
      for armours in armour:
         print('{}:\t Price: {}@, \tArmour: {}' .format(armours, armour[armours]['Buy'], armour[armours]['armour']))

      print()

      for p in pants:
         print('{}:\t Price: {}@, \tArmour: {}' .format(p, pants[p]['Buy'], pants[p]['armour']))

      
      
   
   def trinketShop(self):
      print('How can I help you? I\'m Jonbam.')


class Shop:
   def armourShop()


class GameEngine:
   def signPost(self):
      print('You, {}, find yourself at a sign post.' .format(Hero.name))
      print('''Places to go:
"1" (Armour Shop)
"2" (Forest)
"3" (Inn)''')
      navigation = input('')

      if navigation == '1':
         return Shop().armourShop()

      elif navigation == '2':
         return Shop().forest()
         
      elif navigation == '3':
         return Shop().inn()

      








