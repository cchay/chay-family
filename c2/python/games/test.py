import random, time, sys

class player:
   def __init__(self, 'Bradley'):
      self.hp = 35
      self.name = name
      self.inventory = []
      self.armour = {'head': 'none',
                     'left hand': 'none',
                     'torso': 'none',
                     'legs': 'none',
                     'feet': 'none'}

      self.weapon = 'none'

   def get_hurt(self, damage):
      self.hp -= damage
      print('{} received {} damage.' .format(self.name, self.damage))
