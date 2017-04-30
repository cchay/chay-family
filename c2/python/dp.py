import random, time, sys

class player:
   def __init__(self):
      self.name = 'DiamondPython'
      self.hp = 35
      self.level = 1
      self.xp = 0

      self.level_cost = {2: 1000,
                         3: 5000,
                         4: 10000,
                         5: 20000,
                         6: 50000}

      self.attributes = {'strength': 1,
                         'agility': 1}

      self.skills = {'dodge': {'level': 1},
                     'slash': {'damage': 3, 'level': 1}}

   def getHurt(self, damage):
      self.hp -= damage
      return '{} received {} crushing damage!' .format(self.hp, damage)     

   def winBattle(self):
      xpGain = random.randint(100, 300)
      self.xp += xpGain
      return '{} won the battle and gained {} experience!' .format(self.name, xpGain)

   def loseBattle(self):
      xpGain = random.randint(50, 100)
      self.xp += xpGain
      return '{} lost and gained {} experience...' .format(self.name, xpGain)

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
''' .format(self.name, self.hp, self.level, self.hp, self.level_cost[self.level+1], self.attributes['strength'],
            self.attributes['agility'], self.skills['dodge']['level'], self.skills['slash']['level'])




class dearc:
   def __init__(self):
