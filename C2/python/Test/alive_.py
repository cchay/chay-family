import random

class object:
   def __init__(self, name):
      self.name = name
      self.hp = 5
      self.status = 'ready'

      self.agility = 1
      self.strength = 2
      
      self.skill = 1
      self.dodge = 1

      self.weapon = 'knife'
      self.damage = 2


   def __str__(self):
      return '''    Name        Hitpoints     Status
{}        {}             {}''' .format(self.name, self.hp, self.status)

   def seeIfAlive(self):
      if self.hp < 1:
         self.hp = 0
         self.status = 'struck down'

class fightingGroup():
   def __init__(self, attackers, defenders):    
      self.attacker_total = attackers
      self.defender_total = defenders

      self.attacker_ready = self.attacker_total
      self.defender_ready = self.defender_total

      self.attacker_done = []
      self.defender_done = []


g1 = object('Robber1')
g2 = object('Robber2')
g3 = object('Robber3')
g4 = object('Robber4')
g5 = object('Robber5')

h1 = object('Fallhaven')
h2 = object('Crossglen')
h3 = object('Feygard')


defenders = [g1, g2, g3, g4, g5]
attackers = [h1, h2, h3]

forest = fightingGroup(attackers, defenders)

def battle():
   
   if len(forest.attacker_total) == 0:
      print('You didn\'t finish the quest!')
      
   if len(forest.attacker_total) > 0:
      for i in forest.attacker_ready:
         #forest.attacker_now.remove(i)
         defender = forest.defender_total[random.randint( 0, len( forest.defender_total )-1 )  ]
         print(i.name, 'has hit', defender.name)

   if len(forest.defender_total) > 0:

      for i in forest.defender_ready:
         print('\n',  i.name ,'\n')

      for i in forest.defender_done:
         print('\n',  i.name ,'\n')
      
      for i in forest.defender_ready:
         defender = forest.defender_ready[random.randint(0, len( forest.defender_ready )-1)]        
         attacker = forest.attacker_total[random.randint( 0, len( forest.attacker_total )-1 )  ]        
         print(defender.name, 'has hit', attacker.name)       
         forest.defender_ready.remove(defender)
         forest.defender_done.append(defender)
         
         print('\n',  i.name ,'\n')
   

      
      
battle()













'''
for i in chara:
   i.seeIfAlive()

for i in chara:
   print(i, '\n')

print()
for i in chard:
   i.seeIfAlive()

for i in chard:
   print(i, '\n')

def battle(attr, defr):
   # Skill: The chance you hit your opponent
   # Dodge: The chance you dodge your opponent's blow
   # Strength: The amount of damage you deal
   # Agility: The modifier to the skill 'Dodge'
   
   attack = random.randint(1, 5) + (attr.skill*2)
   defence = random.randint(1, 5) + (defr.dodge*2) + defr.agility
   
   if  attack > defence:
      damage = random.randint(1, attr.damage + attr.strength)
      if defr.hp - damage < 1:
         defr.hp = 0
         defr.status = 'struck down'
         print('{} attacks (Skill/{}/{})\t|\t{}(Dodge/{}) Sucess: {} cutting damage-Struck Down' .format(attr.name, attack, attr.weapon, defr.name, defence, damage))
      else:
         defr.hp -= damage
         print('{} attacks (Skill/{}/{})\t|\t{}(Dodge/{}) Sucess: {} cutting damage' .format(attr.name, attack, attr.weapon, defr.name, defence, damage))
   else:
      print('{} attacks (Skill/{}/{})\t|\t{}(Dodge/{}) Failed' .format(attr.name, attack, attr.weapon, defr.name, defence))

def battleround():
   battle(h1, chard[random.randint(0, 2)])
   for i in chard:
      battle(i, h1)

   for i in chara:
      i.seeIfAlive()

   for i in chara:
      print(i, '\n')

   print()
   for i in chard:
      i.seeIfAlive()

   for i in chard:
      print(i, '\n')
    
'''
