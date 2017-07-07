import random, time, sys


## Changing things: grub -> virus

armour = {'head': {'none': {'name': 'none',
                            'armour': 0,
                            'bprice': 0,
                            'sprice': 0},
                   'bitnbyte helmet': {'name': 'bitnbyte helmet',
                            'armour': 2,
                            'bprice': 10,
                            'sprice': 8},
                   'kilobyte helmet': {'name': 'kilobyte helmet',
                            'armour': 4,
                            'bprice': 50,
                            'sprice': 40},
                   'megabyte helmet': {'name': 'megabyte helmet',
                            'armour': 8,
                            'bprice': 250,
                            'sprice': 200},
                   'gigabyte helmet': {'name': 'gigabyte helmet',
                            'armour': 16,
                            'bprice': 1250,
                            'sprice': 1000},
                   'terrabyte coif': {'name': 'terrabyte helmet',
                            'armour': 32,
                            'bprice': 6250,
                            'sprice': 5000},
                   'technobyte helmet': {'name': 'technobyte helmet',
                            'armour': 64,
                            'bprice': 31250,
                            'sprice': 25000}},
          
          'torso': {'none': {'name': 'none',
                            'armour': 2,
                            'bprice': 25,
                            'sprice': 20},
                    'bitnbyte platemail': {'name': 'bitnbyte platemail',
                            'armour': 4,
                            'bprice': 125,
                            'sprice': 100},
                    'kilobyte platemail': {'name': 'kilobyte platemail',
                            'armour': 8,
                            'bprice': 625,
                            'sprice': 500},
                    'megabyte platemail': {'name': 'megabyte platemail',
                            'armour': 16,
                            'bprice': 3125,
                            'sprice': 2500},
                    'gigabyte platemail': {'name': 'gigabyte platemail',
                            'armour': 32,
                            'bprice': 15625,
                            'sprice': 12500},
                    'terrabyte platemail': {'name': 'terrabyte platemail',
                            'armour': 64,
                            'bprice': 78125,
                            'sprice': 62500},
                    'technobyte platemail': {'name': 'technobyte platemail',
                            'armour': 128,
                            'bprice': 390620,
                            'sprice': 312500}},
          
          'legs': { 'none': {'name': 'none',
                            'armour': 0,
                            'bprice': 0,
                            'sprice': 0},
                    'bitnbyte pants': {'name': 'bitnbyte pants',
                            'armour': 3,
                            'bprice': 15,
                            'sprice': 12},
                    'kilobyte pants': {'name': 'kilobyte pants',
                            'armour': 6,
                            'bprice': 75,
                            'sprice': 60},
                    'megabyte pants': {'name': 'megabyte pants',
                            'armour': 12,
                            'bprice': 375,
                            'sprice': 300},
                    'gigabyte pants': {'name': 'gigabyte pants',
                            'armour': 24,
                            'bprice': 1875,
                            'sprice': 1500},
                    'terrabyte pants': {'name': 'terrabyte pants',
                            'armour': 48,
                            'bprice': 9375,
                            'sprice': 7500},
                    'technobyte pants': {'name': 'technobyte pants',
                            'armour': 96,
                            'bprice': 46875,
                            'sprice': 37500}},
          
          'feet': { 'none': {'name': 'none',
                            'armour': 0,
                            'bprice': 0,
                            'sprice': 0},
                    'bitnbyte boots': {'name': 'bitnbyte boots',
                            'armour': 1,
                            'bprice': 5,
                            'sprice': 4},
                    'kilobyte boots': {'name': 'kilobyte boots',
                            'armour': 2,
                            'bprice': 25,
                            'sprice': 10},
                    'megabyte boots': {'name': 'megabyte boots',
                            'armour': 4,
                            'bprice': 125,
                            'sprice': 100},
                    'gigabyte boots': {'name': 'gigabyte boots',
                            'armour': 8,
                            'bprice': 625,
                            'sprice': 500},
                    'terrabyte boots': {'name': 'terrabyte boots',
                            'armour': 16,
                            'bprice': 3125,
                            'sprice': 2500},
                    'technobyte boots': {'name': 'technobyte boots',
                            'armour': 32,
                            'bprice': 15625,
                            'sprice': 12500}},
          
          'hands': {'none': {'name': 'none',
                            'armour': 0,
                            'bprice': 0,
                            'sprice': 0},
                    'bitnbyte gloves': {'name': 'bitnbyte gloves',
                            'armour': 1,
                            'bprice': 5,
                            'sprice': 4},
                    'kilobyte gloves': {'name': 'kilobyte gloves',
                            'armour': 2,
                            'bprice': 125,
                            'sprice': 100},
                    'megabyte gloves': {'name': 'megabyte gloves',
                            'armour': 4,
                            'bprice': 625,
                            'sprice': 500},
                    'gigabyte gloves': {'name': 'gigabyte gloves',
                            'armour': 8,
                            'bprice': 3125,
                            'sprice': 2500},
                    'terrabyte gloves': {'name': 'terrabyte gloves',
                            'armour': 16,
                            'bprice': 15625,
                            'sprice': 12500},
                    'technobyte gloves': {'name': 'technobyte gloves',
                            'armour': 32,
                            'bprice': 78125,
                            'sprice': 62500}}}

class player:
   def __init__(self):
      self.name = 'DiamondPython'
      self.maxhp = 75
      self.hp = 75
      self.level = 1
      self.xp = 9900
      self.bit = 1000000000000

      self.level_cost = {2: 10000,
                         3: 50000,
                         4: 100000,
                         5: 200000,
                         6: 500000}

      self.attributes = {'strength': 1,
                         'agility': 1}

      self.skills = {'dodge': {'level': 1, 'cost': 5},
                     'slash': {'damage': 10, 'level': 1, 'cost': 5}}
                     #Slash skill damage increases by 50% every level
                     #Dodge and slash skill cost increases by 75%
      self.atttype = 'slashed'

      self.armour = {'head': armour['head']['none'], #armour['head']['technobyte helmet'],
                     'torso': armour['torso']['bitnbyte platemail'],#armour['torso']['technobyte platemail'],
                     'legs': armour['legs']['bitnbyte pants'],#armour['legs']['technobyte pants'],
                     'feet': armour['feet']['none'], #armour['feet']['technobyte boots'],
                     'hands': armour['hands']['none']} #armour['hands']['technobyte gloves']}

      self.resistance  = self.armour['head']['armour'] + self.armour['torso']['armour'] + self.armour['legs']['armour']\
                         + self.armour['feet']['armour'] + self.armour['hands']['armour']

      
      self.inventory = ['bitnbyte helmet']

      self.weapon = 'byteblade'
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
      return '{} lost and gained {} experience...' .format(self.name, xpGain)


   def equipArmour(self, local, item):
      self.resistance -= self.armour[local]['armour']
      self.armour[local] = armour[local][item]
      self.resistance += armour[local][item]['armour']


   def unequipArmour(self, local, item):
      self.resistance -= self.armour[local]['armour']
      self.inventory = (self.armour[local]['name'])
      self.armour[local] = armour[local]['none']


   def levelUp(self):
      self.xp -= self.level_cost[self.level+1]
      if self.xp < 0:
         self.xp = 0
      self.level += 1
      print('Congradulations!! {} has just leveled up!! Good work.' .format(self.name))


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
            self.skills['slash']['damage'], self.resistance, self.armour['head']['name'], self.armour['torso']['name'],
            self.armour['legs']['name'], self.armour['feet']['name'], self.armour['hands']['name'])





dp = player()
print(dp)


def winBattle(xp, bit):
   dp.xp += xp
   dp.bit += bit
   print( '{} received {} exp and {} bits. Good work!' .format(dp.name, xp, bit))
   if dp.xp >= dp.level_cost[dp.level+1]:
      return dp.levelUp()



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
         return technovillage().signpost()
            
      

   def turn(self, a, d, skill):
      if skill == 'slash':
         damagetype = 'cutting'
      else:
         damagetype = 'crushing'
      
      attackchance = random.randint(1, a.skills[skill]['level']) + random.randint(1, 6)
      defendchance = random.randint(1, a.skills['dodge']['level']) + random.randint(1, 6)
      if attackchance > defendchance:
         damagedealt = random.randint(1, int(a.skills[skill]['damage']))
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
      print('Places to go: "s"tore, "f"ileinn, "t"rashbin, "h"ome')

      nav = input('^&: ')
      if nav == "s":
         return technovillage().downloadstore()

      elif nav == "f":
         return technovillage().fileinn()

      elif nav == "t":
         return technovillage().trashbin()

      elif nav == "stats":
         print(dp)
         input('<*Press ENTER to continue*>')
         return technovillage().signpost()

      elif nav == "h":
         return technovillage().home()

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
            
         else:
            print('Uhoh, looks like you don\'t have enough bits. Talk to Lena and she will heal you for half price.')
            print('But only if you\'re level is lower than 5.')
            input('<*Press ENTER to continue*>')
            technovillage().signpost()
            
      elif action == "no":
         print('Aww-right, come again soon!!')
         technovillage().signpost()
         
      else:
         return technovillage().fileinn()

   def downloadstore(self):
      armourlist = []
      #This is where you buy and sell items
      print('Hey, welcome to the download store! download any armour you like!')
      for i in armour:
         for x in armour[i]:
            if x == 'none':
               continue
            print('{}: \tCost: {}, \tArmour: {}' .format(armour[i][x]['name'], armour[i][x]['bprice'], armour[i][x]['armour']))

      action = input('What would you like to buy? ')
      for i in armour:
         for x in armour[i]:
            armourlist.append(armour[i][x]['name'])

      if action in armourlist:
         print('Would you like to buy the {}? ("yes" or "no")' .format(action))
         answer = input('Answer: ')

         if answer == 'yes':
            if dp.bit >= armour[i][x]['bprice']:
               dp.inventory.append(armour[i][x]['name'])
               print('Item purchased successfully!')
               input('<*Press ENTER to continue*>')
               return technovillage().downloadstore()
            else:
               print('I\'m sorry but you do not have enough money')
               input('<*Press ENTER to continue*>')
               return technovillage().downloadstore()
                           

         elif answer == 'no':
            return technovillage().downloadstore()
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
         print('We don\'t have {} here.' .format(action))
         return technovillage().downloadstore()

      return technovillage().downloadstore()
      

            
      

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
      print('You go to your simple hut just outside town.')
      print('here you can equip and unequip armour and later, weapons.')
      action = input('Actions: "u"nequip armour, "e"quip armour, "v"iew storage and gear, "c"heck stats, "b"ack to town')

      if action == "u":
         print('Which armour do you want to unequip?')
         unequip = input()
         local = input('Where?')

         dp.unequipArmour(local, unequip)
         print('You equip the {} on your {}' .format(unequip, local))
         input('<Press enter to continue>')
         return technovillage().home()

      elif action == "e":
         armour = input('What would you like to equip?')
         local = input('Where? ')
         dp.equipArmour(local, armour)
         print('You equip the {} on your {}' .format(armour, local))
         input('<Press enter to continue>')
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

      else:
         input('<Press enter to continue>')
         return technovillage().home()
      
      
      

technovillage().signpost()
