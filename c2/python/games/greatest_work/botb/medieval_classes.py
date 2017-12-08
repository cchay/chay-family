import random, time, sys

class human:
	def __init__(self):
		self.hp = 100
		self.race = "Human"
		self.rhand = "nothing"


class archer(human):
	def __init__(self):
		human.__init__(self)
		self.hp *= 0.75
		self.bothhand = "Long Bow"


class warrior(human):
	def __init__(self):
		human.__init__(self)
		self.hp *= 2
		self.rhand = "War Axe"

			
class knight(human):
	def __init__(self):
		human.__init__(self)
		self.hp *= 1.5
		self.rhand = "Long Sword"
		self.lhand = "shield"


class hunter(human):
	def __init__(self):
		human.__init__(self)
		self.hp *= 0.8
		self.bothhand = "Short Bow"


print(archer().bothhand)
print(warrior().rhand)
print(knight().rhand)
print(hunter().bothhand)
