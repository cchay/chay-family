import random
import time


print('PM CORPORATION PRESENTS:...')
time.sleep(1)
print('SimulationFighter version1.1!!!')

def fightingRound():
	name = input("What is your name? ")
	time.sleep(1)
	print('Okay ' + name + ', choose your opponent.')
	
	fighter = input("""John Cage
Jack Dempsey
Rhonda Rousey
Or you can create your own opponent: 
""")
	print(name + ', your objective in this game is to defeat ' + fighter )
	myHealth = 10
	myEnergy = 20
	fighterHealth = 10
	fighterEnergy = 20
	print(name + ' has ', myHealth, ' health  and ', myEnergy, ' stamina points')
	time.sleep(2)
	print(fighter + ' has ', fighterHealth, ' health and ', fighterEnergy, ' stamina points.')
	time.sleep(2)
	
	print('''punching costs 3 stamina and does 2 damage.
kicking costs 5 stamina and does 4 damage.
suplex costs 15 stamina and does 6 damage.
increasing your health gives you +3 health.
regaining your energy gives you +5 stamimna.
For your attacks, you need to have 1 extra stamina or you do nothing..
''')
	print('If your stamina is too low, than you will not be able to do anything but to regain stamina or increase health.')
	print('You will not do anything if you have incorrect spelling, or if you have little or no stamina.')
	go = input("Good luck. <press enter to continue>")


	while fighterHealth > 0:
		time.sleep(2)
		
		attack = input('''The available commands are:
"punch" 
"kick"
"suplex"
"regain stamina"
"increase health"
''')
		if myEnergy < 4:
			print('You don\'t have enough stamina to attack.')
		time.sleep(2)
		if attack == "punch" and myEnergy > 3:
			print(name + " has punched " + fighter)
			myEnergy = myEnergy - 3
			fighterHealth = fighterHealth - 2
		elif attack == "suplex" and myEnergy >15:
			print(name + ' has done a suplex on ' + fighter)
			myEnergy = myEnergy - 15
			fighterHealth = fighterHealth - 5
		elif attack == "kick" and myEnergy > 5:
			print( name + " has kicked " + fighter)
			myEnergy = myEnergy - 4
			fighterHealth = fighterHealth - 2
		elif attack == "regain stamina":
			print( name + " has regained stamina.")
			myEnergy = myEnergy + 5
		elif attack == "increase health" and myEnergy > 1:
			print(name + ' has regained health')
			myEnergy = myEnergy - 1
			myHealth = myHealth + 3
		elif attack == "":
			print("You do nothiing")
		else:
			print("You have not enough stamina")
			turn()


		chance = random.randint(1,2)

		if fighterEnergy > 15:
			print(fighter + ' has done a suplex to ' + name)
			fighterEnergy = fighterEnergy - 15
			myHealth = myHealth - 5
		elif fighterEnergy < 6:
			print(fighter + ' has regained stamina.')
			fighterEnergy = fighterEnergy + 5
		elif fighterHealth < 4:
			fighterHealth = fighterHealth + 2
			print(fighter + ' has increased health.')
		elif chance == 1 and fighterEnergy > 3:
			myHealth = myHealth -2
			fighterEnergy = fighterEnergy - 3
			print(fighter + ' has punched ' + name + '!')
		elif chance == 2 and fighterEnergy > 5:
			myHealth = myHealth - 4
			fighterEnergy = fighterEnergy - 5 
			print(fighter + ' has kicked ' + name + '!')


		print(name + ' has ', myHealth, ' health points left.' )
		time.sleep(1)
		print(name + ' has ', myEnergy, ' stamina points left')
		time.sleep(2)
		print(fighter + ' has ', fighterHealth ,' health points left.' )
		time.sleep(1)
		print(fighter + ' has ', fighterEnergy ,' stamina points left.')
		time.sleep(2)

		if fighterHealth <= 0:
			print(fighter + ' has been knocked out!!')
			break
		elif myHealth <= 0:
			print(name + ' has been knocked out!!')
			break
		else:
			print('')

fightAgain = "yes"
while fightAgain == "yes" or fightAgain == "y":
        
   fightingRound()

print('do you want to fight again?.')
print('Type "yes" or "y" to play again.')
fightAgain = input()
