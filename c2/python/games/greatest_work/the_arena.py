import random, time, sys

class Hero():
   def __init__(self, name, weapon):
      self.name = name
      self.max_hp = 100
      self.hp = 100
      
      self.weapon = weapon
      
      self.strength = 10
      self.agility = 10
      
      self.attack_speed = 1
      self.status = "Perfect Health"
      
   
   def adjustStatus(self):
   	if self.hp > int(round(self.max_hp*0.8)):
   		self.status = "Perfect Health"
   		
   	elif (self.hp > int(round(self.max_hp*0.3))):
   		self.status = "Wounded"
   		
   	else:
   		self.status = "Severely Wounded"
   
   
   def __str__(self):
   	return '''
Name: {}
Hitpoints: {}

Strength: {}
Agility:  {}

Weapon: {}

''' .format(self.name, self.hp, self.strength, self.agility, self.weapon)


p1 = Hero(input('Player 1, Name: '), input('Player 1, Weapon: '))
p2 = Hero(input('Player 2, Name: '), input('Player 2, Weapon: '))

def getstats(player):

   stat = 0
   while stat != "strength" and stat != 'agility':
      print('Which stat will you increase, {}? strength or agility?' .format(player.name))
      stat = input('')
      if 'strength' in stat:
         player.strength += 5
         player.max_hp += 100
         player.hp += 100
      elif 'agility' in stat:
         player.agility += 5
         player.attack_speed += 1

getstats(p1)
getstats(p2)

print(p1)
print()
print(p2)


def battle(p1, p2):
	while p1.hp >= 0 and p2.hp >= 0:
		input()
		print('---------------------------------------------------------------------------------------')
		print('{}\t{}\t{}' .format(p1.name, p1.status, p1.hp))
		print('{}\t{}\t{}' .format(p2.name, p2.status, p2.hp))
		
		print('***************************************************************************************')
		
		
		battleRound(p1, p2)
		battleRound(p2, p1)
		
		p1.adjustStatus()
		p2.adjustStatus()
	
	else:
		if p1.hp <= 0:
			print('{} has been knocked out!!' .format(p1.name))
			
		elif p2.hp <= 0:
			print('{} has been knocked out!!' .format(p2.name))
			
		else:
			print('{} and {} have been knocked out!!' .format(p1.name, p2.name))
		
		print('---------------------------------------------------------------------------------------')
		print('{}\t{}\t{}' .format(p1.name, p1.status, p1.hp))
		print('{}\t{}\t{}' .format(p2.name, p2.status, p2.hp))


def battleRound(p1, p2):
	## p1 attacks
	
	for i in range(p1.attack_speed):
		damage = random.randint(1, 10)+random.randint(1, p1.strength)
		attack_chance = random.randint(1, 10) * random.randint(1, 6)
		
		defence_chance = random.randint(1, p2.agility) * random.randint(1, 6)
		
		if attack_chance > defence_chance:
			p2.hp -= damage
			print('!{} strikes with their {}({}) : {} fails to dodge({})!     -{} damage' .format(p1.name, p1.weapon, attack_chance, p2.name, defence_chance, damage))
			
		else:
			print('!{} strikes with their {}({}) : {} easily dodges({})!' .format(p1.name, p1.weapon, attack_chance, p2.name, defence_chance))
			


battle(p1, p2)











