import random, time, sys, pickle


##                                           Game goals:

## raising skill levels next on list ****
## @!DONE!@!Merge pickle with this to start having savesss *****!
## Create login and signup page for multiple accounts so many people can play the game
## Create a weapon dictionary: spears, maces, swords, axes, bows **
## @!DONE!@Create a pickle data file for armour dictionary ****
## Create a pickle data file for weapon dictionary
## @!DONE!@Create a function to delete things in inventory or create a sell option in the store

##															Game EM. Todos:

## @!FIXED!@ Fix KeyError in technobyte_village().home(). equip gear
## @!FIXED!@ Fix inventory append stuff 
## @!FIXED!@ Fix hp increase when level up (It dosen't do that right now)
## @!FIXED!@ Fix buy items and inventory glitch
## @!FIXED!@ Fix Armour disappearance when armour is equipped
## @!FIXED!@ Alerts a keyError when there isn't one.



player_profile = pickle.load(open('rpg-techno-game-data.pickle', 'rb'))
armourdata = pickle.load(open('armourdata.pickle', 'rb'))
weapondata = pickle.load(open('weapondata.pickle', 'rb'))


class player:
   def __init__(self, player_profile):
      self.name = player_profile['name']
      self.maxhp = player_profile['maxhp']
      self.hp = player_profile['hp']
      self.level = player_profile['level']
      self.xp = player_profile['xp']
      self.bit = player_profile['bits']
      self.inventory = player_profile['inventory']
      self.wdamage = player_profile['wdamage']

      self.weapon = player_profile['weapon']

      self.level_cost = {2: 10000,
                         3: 50000,
                         4: 100000,
                         5: 200000,
                         6: 500000}
      
      self.hpinc = {2: 131,
                    3: 229,
                    4: 401,
                    5: 702,
                    6: 1228}

      self.attributes = player_profile['attributes']
                        # Player gets 2 skill points per level maybe 1


      self.skills = {'dodge': {'level': 1, 'cost': 5},#{'level': 1, 'cost': 5},
                     'slash': {'damage': 10, 'level': 1, 'cost': 5}}#{'damage': 10, 'level': 1, 'cost': 5}}
                     #Slash skill damage increases by 50% every level
                     #Dodge and slash skill cost increases by 75%
      
      self.atttype = 'slashed'

      self.weapons = {'bothhands': 0, #nothing yetttt
                      'lefthand': 0,  #not yet
                      'right hand': 0}

      '''self.armour = {'head': armour['head']['none'], #armour['head']['technobyte helmet'],
                     'torso': armour['torso']['bitnbyte platemail'],#armour['torso']['technobyte platemail'],
                     'legs': armour['legs']['bitnbyte pants'],#armour['legs']['technobyte pants'],
                     'feet': armour['feet']['none'], #armour['feet']['technobyte boots'],
                     'hands': armour['hands']['none']} #armour['hands']['technobyte gloves']}'''

      self.armour = player_profile['armour']

      self.resistance  = self.armour['head']['armour'] + self.armour['torso']['armour'] + self.armour['legs']['armour']\
                         + self.armour['feet']['armour'] + self.armour['hands']['armour']
   
      self.totdamage = 0

      
   def getHurt(self, damage):
      self.hp -= damage
      if self.hp <= 0:
         return '{} received {} crushing damage and has died!! But fortunately you were dragged to safety.' .format(self.name, damage)
      else:
         return '{} received {} crushing damage!' .format(self.name, damage)


   def loseBattle(self):
      xpGain = random.randint(50, 100)
      self.xp += xpGain
      player_profile['exp'] += xpGain
      return '{} lost and gained {} experience...' .format(self.name, xpGain)


   def equipArmour(self, local, item):
      player_profile['inventory'].append(self.armour[local]['name'])
      self.resistance -= self.armour[local]['armour'] #This adjusts the armour bonus before equiping the new armour
      self.armour[local] = armourdata[local][item]# Equips the new armour and discards the old
      self.resistance += armourdata[local][item]['armour']# Readjusts the new armour stats
      player_profile['resistance'] += armourdata[local][item]['armour']
      player_profile['armour'][local] = armourdata[local][item]
      player_profile['inventory'].remove(self.armour[local]['name'])
      if 'none' in player_profile['inventory']:
         player_profile['inventory'].remove('none')
      


   def unequipArmour(self, local, item):
      self.resistance -= self.armour[local]['armour']
      #self.inventory.append(self.armour[local]['name'])
      self.armour[local] = armourdata[local]['none']
      player_profile['resistance'] -= self.armour[local][item]['armour']
      player_profile['armour'][local] = armourdata[local]['none']
      player_profile['inventory'].append(self.armour[local]['name'])
   
   
   def equipWeapon(self, item):
      player_profile['inventory'].append(self.weapon) #stores the old weapon
      self.weapon = item# Equips the weapon
      self.wdamage = weapondata[item]['damage']
      player_profile['wdamage'] = weapondata[item]['damage']
      player_profile['weapon'] = item
      player_profile['inventory'].remove(item)
      if 'none' in player_profile['inventory']:
         player_profile['inventory'].remove('none')
      


   def unequipWeapon(self, item):
      self.wdamage = 0
      #self.inventory.append(self.weapon)
      self.weapon = 'none'
      player_profile['wdamage'] = 0
      player_profile['weapon'] = 'none'
      player_profile['inventory'].append(item)


   def levelUp(self):
      self.xp -= self.level_cost[self.level+1]
      if self.xp < 0: # making sure there are no errors in the code, Will have to take this out alter 
         self.xp = 0
      self.level += 1
      self.maxhp = self.hpinc[self.level]
      player_profile['maxhp'] = self.hpinc[self.level]
      print('Congradulations!! {} has just leveled up!! Good work.' .format(self.name))
      
      player_profile['xp'] = self.xp
      player_profile['level'] = self.level
      player_profile['attributes']['strength'] += 1
      player_profile['attributes']['agility'] += 1
      dp.attributes['strength'] += 1
      dp.attributes['agility'] += 1


   def displayInv(self):
      for i in self.inventory:
         print(i)
      

   def __str__(self):
      return '''
STATS:

Name: {}
   HP: {}
   Level: {}
   XP: {}/{}
   Bits: {}

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
''' .format(self.name, self.hp, self.level, self.xp, self.level_cost[self.level+1], self.bit, self.attributes['strength'],
            self.attributes['agility'], self.skills['dodge']['level'], self.skills['slash']['level'], self.weapon,
            self.skills['slash']['damage'] + self.wdamage, self.resistance, self.armour['head']['name'], self.armour['torso']['name'],
            self.armour['legs']['name'], self.armour['feet']['name'], self.armour['hands']['name'])







dp = player(player_profile)


def winBattle(xp, bit):
   dp.xp += xp
   dp.bit += bit
   print( '{} received {} exp and {} bits. Good work!' .format(dp.name, xp, bit))
   if dp.xp >= dp.level_cost[dp.level+1]:
      return dp.levelUp()
   
   player_profile['xp'] = dp.xp
   player_profile['bits'] = dp.bit
   



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



class battle:
   def fight(self, a, d):
      a.totdamage = 0
      print('{}: {}' .format(a.name, a.hp))
      print('{}: {}' .format(d.name, d.hp))
      while a.hp > 0 and d.hp > 0:
         
         battle().turn(a, d, 'slash')
         battle().turn(d, a, 'smash')
         #print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
         #input('<press enter to continue>')

      else:
         if a.hp <= 0 and d.hp <= 0:
            print('{} and {} have died from their numerous wounds.' .format(a.name, d.name))

         elif a.hp <= 0:
            print('{} has been killed.' .format(a.name))

         elif d.hp <= 0:
            print('{} has been killed.' .format(d.name))
            winBattle(d.xp, d.bit)

         print('{}: {}' .format(a.name, a.hp))
         print('{}: {}' .format(d.name, d.hp))
         print('{} received {} damage and dealt {} damage.' .format(a.name, a.totdamage, d.totdamage))
         input('<*Press ENTER to continue*>')
         player_profile['hp'] = a.hp
         return technovillage().signpost()
            
      

   def turn(self, a, d, skill):
      if skill == 'slash':
         damagetype = 'cutting'
      else:
         damagetype = 'crushing'
      
      attackchance = random.randint(1, a.skills[skill]['level']) + random.randint(1, 6)
      defendchance = random.randint(1, a.skills['dodge']['level']) + random.randint(1, 6)
      if attackchance > defendchance:
         damagedealt = random.randint(1, int(a.skills[skill]['damage'])) + a.wdamage
         damagedealt += random.randint(0, 6)
         damagedealt -= d.resistance
         if damagedealt <= 0:
            damagedealt = 0
         d.totdamage += damagedealt
         #print('{} {} {} for {} {} damage!!!!' .format(a.name, a.atttype, d.name, damagetype, damagedealt))
         d.hp -= damagedealt

      else:
         pass
         #print('{} missed!' .format(a.name))


class technovillage:
   def signpost(self):
      print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
      print('You find yourself at a sign post at the center of Technovillage. Where\'d you like to go?')
      print('Places to go: "as"(armour store), "ws"(weapon store), "am"(armour market, sell armours here), "wm"(weapon market, sell weapons here), "f"ileinn, "t"rashbin, "h"ome, "save" to save the game, or "quit" to exit the game')

      nav = input('^&: ')
      if nav == "as":
         return technovillage().downloadstore_buy()
      
      if nav == "ws":
         return technovillage().buyweapons()

      elif nav == "f":
         return technovillage().fileinn()

      elif nav == "t":
         return technovillage().trashbin()
      
      elif nav == "am":
         return technovillage().downloadstore_sell(armourdata)
      
      elif nav == "wm":
         return technovillage().sellweapons()

      elif nav == "stats":
         print(dp)
         input('<*Press ENTER to continue*>')
         return technovillage().signpost()

      elif nav == "h":
         return technovillage().home()
      
      elif nav == "quit":
         with open('rpg-techno-game-data.pickle', 'wb') as h:
            pickle.dump(player_profile, h) 
         print('Saving and quitting...')
         sys.exit()
      
      elif nav == "save":
         with open('rpg-techno-game-data.pickle', 'wb') as h:
            pickle.dump(player_profile, h) 
         print('Saving...')
         input('Saved.')
         return technovillage().signpost()

      else:
         return technovillage().signpost()
         
   
   def fileinn(self):
      # You can rest and restore your hp here
      price = int(round(10 + 0.1*dp.level))
      print('"Good reboot to you! Fileinn at your service! We\'ve got the most comfortable beds in all Computa!"')
      print('"Would you like a room? It only costs {} bits and all your hp gets recovered."' .format(price))
      print('You can type "yes" to sleep or "no" to leave.')
      action = input('Answer:')

      if action == 'yes':
         if dp.bit >= price:
            print('You sleep in an extremely comfortable bed and wake up bright and early the next day.')
            print('"Good reboot! Hope you slept well."')
            input('<*Press ENTER to continue*>')
            dp.bit -= price
            dp.hp = dp.maxhp
            technovillage().signpost()
            
            player_profile['bits'] = dp.bit
            player_profile['hp'] = dp.hp
            
         else:
            print('Uhoh, looks like you don\'t have enough bits. Talk to Lena and she will heal you for half price.')
            print('But only if your level is lower than 5.')
            input('<*Press ENTER to continue*>')
            technovillage().signpost()
            
      elif action == "no":
         print('Aww-right, come again soon!!')
         technovillage().signpost()
         
      else:
         return technovillage().fileinn()

   def downloadstore_buy(self):
      armourlist = []
      #This is where you buy and sell items
      print('Hey, welcome to the download store! Download any armour you like!')
      print('Or type "leave" to leave')
      for i in armourdata:
         for x in armourdata[i]:
            if x == 'none':
               continue
            print('{}: \tCost: {}, \tArmour: {}' .format(armourdata[i][x]['name'], armourdata[i][x]['bprice'], armourdata[i][x]['armour']))

      action = input('What would you like to buy? ')
      for i in armourdata:
         for x in armourdata[i]:
            armourlist.append(armourdata[i][x]['name'])

      if action in armourlist:
         print('Would you like to buy the {}? ("yes" or "no")' .format(action))
         answer = input('Answer: ')
         item = action

         if answer == 'yes':
            if dp.bit >= armourdata[i][x]['bprice']:
               dp.bit -= armourdata[i][x]['bprice']
               #dp.inventory.append(item) Doubled the items I bought for the price of 1
               player_profile['inventory'].append(item)
               player_profile['bits'] = dp.bit
               print('Item purchased successfully!')
               input('<*Press ENTER to continue*>')
               return technovillage().downloadstore_buy()
            else:
               print('I\'m sorry but you do not have enough money')
               input('<*Press ENTER to continue*>')
               return technovillage().downloadstore_buy()
                           

         elif answer == 'no':
            return technovillage().downloadstore_buy()
            input('<*Press ENTER to continue*>')

         elif answer == "leave":
            print('You leave the armour shop')
            input('<*Press ENTER to continue*>')
            return technovillage().signpost()
                     
      if action == 'leave':
         print('You leave the armour shop')
         input('<*Press ENTER to continue*>')
         return technovillage().signpost()
                     
      if not action in armourlist:
         item = action
         print('We don\'t have {} here.' .format(item))
         return technovillage().downloadstore_buy()

      return technovillage().downloadstore_buy()
   
   
   
   def downloadstore_sell(self, data):
      print('Please select an item in your inventory you would like to sell:')
      for i in dp.inventory:
         print(i)
      item = input('ITEM^^): ')
      if item == "leave":
         return technovillage().signpost()
      
      local = input('Location^^): ')
      
      if item in dp.inventory:
         print('you sell the {} for {} bits.' .format(item, data[local][item]['sprice']))
         dp.bit += data[local][item]['sprice']
         player_profile['bits'] += data[local][item]['sprice']
         player_profile['inventory'].remove(item)
         #dp.inventory.remove(item)
         return technovillage().downloadstore_sell(data)
      
      elif not item in dp.inventory:
         print('I\'m sorry, but you don\'t have {} in your inventory.' .format(item))
         return technovillage().downloadstore_sell(data)
      
      else:
         return technovillage().downloadstore_sell(data)
      
      print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
      
      
      
   def buyweapons(self):
      weaponlist = []
      #This is where you buy and sell items
      print('Hey, welcome to the download store! Download any armour you like!')
      print('Or type "leave" to leave')
      for i in weapondata:
         if i == 'none':
            continue
         print('{}: \tCost: {}, \tArmour: {}' .format(weapondata[i]['name'], weapondata[i]['bprice'], weapondata[i]['damage']))

      action = input('What would you like to buy? ')
      for i in weapondata:
         weaponlist.append(weapondata[i]['name'])

      if action in weaponlist:
         print('Would you like to buy the {}? ("yes" or "no")' .format(action))
         answer = input('Answer: ')
         item = action

         if answer == 'yes':
            if dp.bit >= weapondata[i]['bprice']:
               dp.bit -= weapondata[i]['bprice']
               #dp.inventory.append(item) Doubled the items I bought for the price of 1
               player_profile['inventory'].append(item)
               player_profile['bits'] = dp.bit
               print('Item purchased successfully!')
               input('<*Press ENTER to continue*>')
               return technovillage().buyweapons()
            else:
               print('I\'m sorry but you do not have enough money')
               input('<*Press ENTER to continue*>')
               return technovillage().buyweapons()
                           

         elif answer == 'no':
            return technovillage().buyweapons()
            input('<*Press ENTER to continue*>')

         elif answer == "leave":
            print('You leave the armour shop')
            input('<*Press ENTER to continue*>')
            return technovillage().signpost()
                     
      if action == 'leave':
         print('You leave the armour shop')
         input('<*Press ENTER to continue*>')
         return technovillage().signpost()
                     
      if not action in weaponlist:
         item = action
         print('We don\'t have {} here.' .format(item))
         return technovillage().buyweapons()

      return technovillage().buyweapons()
   
   
   def sellweapons(self):
      print('Please select a weapon in your inventory you would like to sell:')
      for i in dp.inventory:
         if 'sword' in i:
            print(i)
            
      item = input('ITEM^^): ')
      if item == "leave":
         return technovillage().signpost()
      
      
      if item in dp.inventory:
         print('you sell the {} for {} bits.' .format(item, weapondata[item]['sprice']))
         dp.bit += weapondata[item]['sprice']
         player_profile['bits'] += weapondata[item]['sprice']
         player_profile['inventory'].remove(item)
         #dp.inventory.remove(item)
         return technovillage().sellweapons()
      
      elif not item in dp.inventory:
         print('I\'m sorry, but you don\'t have {} in your inventory.' .format(item))
         return technovillage().sellweapons()
      
      else:
         return technovillage().sellweapons()
      
      print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
      
            
      

   def trashbin(self):
      #Fighting area
      print('Welcome to the trashbin. It\'s endless and you can fight virtually anything.')
      print('We only have viruses here. Do you want to fight the virus?')
      answer = input('Answer: ')

      if answer == 'yes':
         bug = virus()
         battle().fight(dp, bug)
         return technovillage().trashbin

      elif answer == 'maybe':
         bug = hacker()
         battle().fight(dp, bug)
         return technovillage().trashbin


      elif answer == "no":
         return technovillage().signpost()
      
      else:
         return technovillage().trashbin()


   def home(self):
      print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
      try:
         print('You go to your simple hut just outside town.')
         print('here you can equip and unequip armour and later, weapons.')
         action = input('Actions: "ua"nequip armour, "ea"quip armour, "v"iew storage and gear, "c"heck stats, "b"ack to town')

         if action == "ua":
            print('Which armour do you want to unequip?')
            unequip = input()
            local = input('Where?')

            dp.unequipArmour(local, unequip)
            print('You unequip the {} on your {}' .format(unequip, local))
            input('<Press enter to continue>')
            return technovillage().home()

         elif action == "ea":
            armour = input('What would you like to equip?')
            local = input('Where? ')
            dp.equipArmour(local, armour)
            print('You equip the {} on your {}' .format(armour, local))
            input('<Press enter to continue>')
            return technovillage().home()
         
         elif action == "ew":
            weapon = input('What weapon would you like to equip?')
            dp.equipWeapon(weapon)
            print('You equip the {}' .format(weapon))
            input('press <ENTER> to continue')
            return technovillage().home()
         
         elif action == "uw":
            weapon = input('What weapon would you like to unequip?')
            dp.unequipWeapon(weapon)
            print('You unequip the {}' .format(weapon))
            input('press <ENTER> to continue')
            return technovillage().home()

         elif action == "v":
		      #print(dp.inventory)
		      #print()
		      #print(dp.armour)

            print('\nInventory:\n')

            for i in dp.inventory:
               print(i)#['name'])
            input('<Press enter to continue>')

            return technovillage().home()

         elif action == "b":
            return technovillage().signpost()

         elif action == "c":
            print(dp)
            input('<Press enter to continue>')
            return technovillage().home()
         
         elif nav == "save":
            with open('rpg-techno-game-data.pickle', 'wb') as h:
               pickle.dump(player_profile, h) 
            print('Saving...')
            input('Saved. :)')
            return technovillage().home()

         else:
            input('<Press enter to continue>')
            return technovillage().home()
		
      except KeyError as e:
         #print('There was a key error, try to type the item or location properly next time.. :(')
         return technovillage().home()
	
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
print(dp)
technovillage().signpost()


with open('rpg-techno-game-data.pickle', 'wb') as h:
  pickle.dump(player_profile, h)
  
with open('weapondata.pickle', 'wb') as h:
  pickle.dump(weapondata, h)

