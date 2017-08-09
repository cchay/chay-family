import random, time, sys, pickle

sys.path.insert(0, '/home/iceman/_/chay-family/c2/python/games/rpg-techno-game/classes')

import login, technovillage, battle, playerprofile

#profile = emptyProfile()



player_profile = pickle.load(open('data/rpg-techno-game-data.pickle', 'rb'))
armourdata = pickle.load(open('data/armourdata.pickle', 'rb'))
weapondata = pickle.load(open('data/weapondata.pickle', 'rb'))


class virus():
   def __init__(self):
      self.hp = 50
      self.name = 'virus'
      self.damage = 10
      self.strength = 1
      self.agility = 1

      self.resistance = 5

      self.skills = {'dodge': {'level': 1},
                     'smash': {'damage': 7, 'level': 1}}
      self.atttype = 'smashed'

      self.xp = 100
      self.bit = random.randint(5, 20)
      self.totdamage = 0
      self.wdamage = 5



class hacker():
   def __init__(self):
      #level 100 or so
      self.hp = 1000
      self.name = 'hacker'
      self.damage = 1000
      self.strength = 100
      self.agility = 100

      self.resistance = 100

      self.skills = {'dodge': {'level': 10},
                     'smash': {'level': 100, 'damage': 700}}
      self.atttype = 'smashed'

      self.xp = 100000
      self.bit = random.randint(5000, 200000)
      self.totdamage = 0
      self.wdamage = 500


player = login.login()
player.welcome()
#name = player.username
print('Username: ', player.name)
dp = playerprofile.player(player_profile, player.name, player.password)
technovillage.technovillage().signpost(dp)



	
def updates():   
   print('UPDATES!!!')
   look = input('type "look" to see the new updates and game goals or type "skip" to skip')
   if look == "look":
      print('''                                    
**************************************************************************************************************
                                                   Game goals:

 raising skill levels next on list
 Create login and signup page for multiple accounts so many people can play the game

2017.8.1
 Created a weapon dictionary: spears, maces, swords, axes, bows
 Created a place to buy and sell weapons
 Adjusted damage dealt to enemy
 Created a save function so you don't have to quit the porgram

2017.7.27

2017.7.26
 Created a pickle data file for armour dictionary 

2017.7.25
 Merged pickel with this to start having saves


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
														         Game bugs and todos:

2017.8.1
 Fixed unequip armour bug

2017.7.27
 Fixed a keyError alert bug in technovillage().home()

2107.7.26
 Fixed hp increase when level up (It dosen't do that right now)
 Fixed buy items and inventory glitch

2017.7.25
 Fixed KeyError in technobyte_village().home(). equip gear
 Fixed inventory append stuff 

***************************************************************************************************************
''')
      
   elif look == "skip":
      pass
   
   else:
      return updates()

#updates()
#input('Press <enter> to advance to the game!!')

#technovillage().signpost()

'''login().welcome()
dp = player(player_profile, player_profile[profile.name], player_profile[profile.name]['password'])
print(dp)
technovillage().signpost()
'''
with open('rpg-techno-game-data.pickle', 'wb') as h:
  pickle.dump(player_profile, h)
  
with open('weapondata.pickle', 'wb') as h:
  pickle.dump(weapondata, h)

