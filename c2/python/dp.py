import random, time, sys

armour = {'head': {'none': {'name': 'none',
                            'armour': 0,
                            'bprice': 0,
                            'sprice': 0},
                   'cloth cap': {'name': 'cloth cap',
                            'armour': 2,
                            'bprice': 10,
                            'sprice': 8},
                   'leather helmet': {'name': 'leather helmet',
                            'armour': 4,
                            'bprice': 50,
                            'sprice': 40},
                   'bronze helmet': {'name': 'bronze helmet',
                            'armour': 8,
                            'bprice': 250,
                            'sprice': 200},
                   'iron helmet': {'name': 'iron helmet',
                            'armour': 16,
                            'bprice': 1250,
                            'sprice': 1000},
                   'chain coif': {'name': 'chain coif',
                            'armour': 32,
                            'bprice': 6250,
                            'sprice': 5000},
                   'steel helmet': {'name': 'steel helmet',
                            'armour': 64,
                            'bprice': 31250,
                            'sprice': 25000}},
          
          'torso': {'none': {'name': 'none',
                            'armour': 2,
                            'bprice': 25,
                            'sprice': 20},
                    'cloth shirt': {'name': 'cloth shirt',
                            'armour': 4,
                            'bprice': 125,
                            'sprice': 100},
                    'leather vest': {'name': 'leather vest',
                            'armour': 8,
                            'bprice': 625,
                            'sprice': 500},
                    'bronze chest plate': {'name': 'bronze shirt',
                            'armour': 16,
                            'bprice': 3125,
                            'sprice': 2500},
                    'iron platemail': {'name': 'iron platemail',
                            'armour': 32,
                            'bprice': 15625,
                            'sprice': 12500},
                    'chainmail shirt': {'name': 'chainmail shirt',
                            'armour': 64,
                            'bprice': 78125,
                            'sprice': 62500},
                    'steel ringmail': {'name': 'steel ringmail',
                            'armour': 128,
                            'bprice': 390620,
                            'sprice': 312500}},
          
          'legs': { 'none': {'name': 'none',
                            'armour': 0,
                            'bprice': 0,
                            'sprice': 0},
                    'cloth leggings': {'name': 'cloth leggings',
                            'armour': 3,
                            'bprice': 15,
                            'sprice': 12},
                    'leather pants': {'name': 'leather pants',
                            'armour': 6,
                            'bprice': 75,
                            'sprice': 60},
                    'bronze greaves': {'name': 'bronze greaves',
                            'armour': 12,
                            'bprice': 375,
                            'sprice': 300},
                    'iron pants': {'name': 'iron pants',
                            'armour': 24,
                            'bprice': 1875,
                            'sprice': 1500},
                    'chainmail pants': {'name': 'chainmail pants',
                            'armour': 48,
                            'bprice': 9375,
                            'sprice': 7500},
                    'steel pants': {'name': 'steel pants',
                            'armour': 96,
                            'bprice': 46875,
                            'sprice': 37500}},
          
          'feet': { 'none': {'name': 'none',
                            'armour': 0,
                            'bprice': 0,
                            'sprice': 0},
                    'cloth shoes': {'name': 'cloth shoes',
                            'armour': 1,
                            'bprice': 5,
                            'sprice': 4},
                    'leather moccasins': {'name': 'leather moccasins',
                            'armour': 2,
                            'bprice': 25,
                            'sprice': 10},
                    'bronze boots': {'name': 'bronze boots',
                            'armour': 4,
                            'bprice': 125,
                            'sprice': 100},
                    'iron boots': {'name': 'iron boots',
                            'armour': 8,
                            'bprice': 625,
                            'sprice': 500},
                    'chainmail socks': {'name': 'chainmail socks',
                            'armour': 16,
                            'bprice': 3125,
                            'sprice': 2500},
                    'steel boots': {'name': 'steel boots',
                            'armour': 32,
                            'bprice': 15625,
                            'sprice': 12500}},
          
          'hands': {'none': {'name': 'none',
                            'armour': 0,
                            'bprice': 0,
                            'sprice': 0},
                    'cloth gloves': {'name': 'cloth gloves',
                            'armour': 1,
                            'bprice': 5,
                            'sprice': 4},
                    'leather gloves': {'name': 'leather gloves',
                            'armour': 2,
                            'bprice': 125,
                            'sprice': 100},
                    'bronze gloves': {'name': 'bronze gloves',
                            'armour': 4,
                            'bprice': 625,
                            'sprice': 500},
                    'iron gloves': {'name': 'iron gloves',
                            'armour': 8,
                            'bprice': 3125,
                            'sprice': 2500},
                    'chainmail gloves': {'name': 'chainmail gloves',
                            'armour': 16,
                            'bprice': 15625,
                            'sprice': 12500},
                    'steel gloves': {'name': 'steel gloves',
                            'armour': 32,
                            'bprice': 78125,
                            'sprice': 62500}}}

class player:
   def __init__(self):
      self.name = 'DiamondPython'
      self.hp = 75
      self.level = 1
      self.xp = 0

      self.level_cost = {2: 10000,
                         3: 50000,
                         4: 100000,
                         5: 200000,
                         6: 500000}

      self.attributes = {'strength': 1,
                         'agility': 1}

      self.skills = {'dodge': {'level': 1},
                     'slash': {'damage': 3, 'level': 1}}

      self.armour = {'head': armour['head']['cloth cap'],
                     'torso': armour['torso']['cloth shirt'],
                     'legs': armour['legs']['cloth leggings'],
                     'feet': armour['feet']['none'],
                     'hands': armour['hands']['none']}

      self.resistance  = self.armour['head']['armour'] + self.armour['torso']['armour'] + self.armour['legs']['armour']\
                         + self.armour['feet']['armour'] + self.armour['hands']['armour']

      
      self.inventory = []

      self.weapon = 'knife'

      
   def getHurt(self, damage):
      self.hp -= damage
      if self.hp <= 0:
         return '{} received {} crushing damage and has died!! But fortunately you were dragged to safety.' .format(self.name, damage)
      else:
         return '{} received {} crushing damage!' .format(self.name, damage)
   

   def winBattle(self):
      xpGain = random.randint(100, 300)
      self.xp += xpGain
      print( '{} won the battle and gained {} experience!' .format(self.name, xpGain))
      if self.xp >= self.level_cost[self.level+1]:
         return player().levelUp()


   def loseBattle(self):
      xpGain = random.randint(50, 100)
      self.xp += xpGain
      return '{} lost and gained {} experience...' .format(self.name, xpGain)


   def equipArmour(self, local, item):
      self.resistance -= self.armour[local]['armour']
      self.armour[local] = armour[local][item]
      self.resistance += armour[local][item]['armour']


   def unequipArmour(self, local, item):
      self.resistance -= self.armour[local]['armour']
      self.inventory.append(self.armour[local]['name'])
      self.armour[local] = armour[local]['none']


   def levelUp(self):
      self.xp -= self.level_cost[self.level+1]
      if self.xp < 0:
         self.xp = 0
      self.level += 1
      return 'Congradulations!! {} has just leveled up!! Good work.' .format(self.name)


   def __str__(self):
      return '''
Name: {}
   HP: {}
   Level: {}
   XP: {}/{}

Attributes:
   Strength: {}
   Agility:  {}

Skills:
   Dodge: level: {}
   Slash: level: {}

Weapon: {}
   Damage: {}

Armour:
   Resistance: {}
      Head: {}
      Torso: {}
      Legs: {}
      Feet: {}
      Hands: {}
''' .format(self.name, self.hp, self.level, self.xp, self.level_cost[self.level+1], self.attributes['strength'],
            self.attributes['agility'], self.skills['dodge']['level'], self.skills['slash']['level'], self.weapon,
            self.skills['slash']['damage'], self.resistance, self.armour['head']['name'], self.armour['torso']['name'],
            self.armour['legs']['name'], self.armour['feet']['name'], self.armour['hands']['name'])



dp = player()
print(dp)
