import time, random

fire = {'name': 'Fire' ,'damage': 14, 'aftershock': 6, 'defence': 5}
ice = {'name': 'Ice' ,'damage': 15, 'aftershock': 4, 'defence': 10}
water = {'name': 'Water' ,'damage': 14, 'aftershock': 3, 'defence': 9}
earth = {'name': 'Earth' ,'damage': 15, 'aftershock': 3, 'defence': 13}
wind = {'name': 'Wind' ,'damage': 13, 'aftershock': 4, 'defence': 5}
lightning = {'name': 'Lightning' ,'damage': 16, 'aftershock': 1, 'defence': 0}
social = {'name': 'Social' ,'damage': 16, 'aftershock': 5, 'defence': 0}


class attack:
   def __init__(self, element):
      self.name = element['name']
      self.damage = element['damage']
      self.aftershock = element['aftershock']
      self.defence = element['defence']

class player:
   def __init__(self, name, attack):
      self.name = name
      
      self.attack = attack
      self.defence = self.attack.defence
      self.aftershock = self.attack.aftershock

   def adjust():
      if self.attack == :
         
      

f1 = input('Okay. Now, Fighter 1, what\'s your name? ')
e1 = input('What element do you want?(social/fire/ice/water/earth/wind/lightning) ')
player(f1, e1)
player.adjust()

f2 = input('Fighter 2, what\'s your name? ')
e2 = input('What element do you want?(social/fire/ice/water/earth/wind/lightning) ')
player(f2, e2)
player.adjust()
      
def game():
   print('Hi, Welcome to the Elemental Wars!! YAY!!!!')
