import random, time, sys


## Changing things: grub -> virus

armour = {'head': {'none': {'name': 'none',
                            'armour': 0,
                            'bprice': 0,
                            'sprice': 0},
                   'byte cap': {'name': 'byte cap',
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
                   'terrabyte coif': {'name': 'terrabyte coif',
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
                    'byte shirt': {'name': 'byte shirt',
                            'armour': 4,
                            'bprice': 125,
                            'sprice': 100},
                    'kilobyte vest': {'name': 'kilobyte vest',
                            'armour': 8,
                            'bprice': 625,
                            'sprice': 500},
                    'megabyte chest plate': {'name': 'megabyte shirt',
                            'armour': 16,
                            'bprice': 3125,
                            'sprice': 2500},
                    'gigabyte platemail': {'name': 'gigabyte platemail',
                            'armour': 32,
                            'bprice': 15625,
                            'sprice': 12500},
                    'terrabyte shirt': {'name': 'terrabyte shirt',
                            'armour': 64,
                            'bprice': 78125,
                            'sprice': 62500},
                    'technobyte ringmail': {'name': 'technobyte ringmail',
                            'armour': 128,
                            'bprice': 390620,
                            'sprice': 312500}},
          
          'legs': { 'none': {'name': 'none',
                            'armour': 0,
                            'bprice': 0,
                            'sprice': 0},
                    'byte pants': {'name': 'byte pants',
                            'armour': 3,
                            'bprice': 15,
                            'sprice': 12},
                    'kilobyte pants': {'name': 'kilobyte pants',
                            'armour': 6,
                            'bprice': 75,
                            'sprice': 60},
                    'megabyte greaves': {'name': 'megabyte greaves',
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
                    'byte shoes': {'name': 'byte shoes',
                            'armour': 1,
                            'bprice': 5,
                            'sprice': 4},
                    'kilobyte moccasins': {'name': 'kilobyte moccasins',
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
                    'terrabyte socks': {'name': 'terrabyte socks',
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
                    'byte gloves': {'name': 'byte gloves',
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
      self.hp = 75
      self.level = 1
      self.xp = 0
      self.bit = 100

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
                     #Dodge and slash skill cost increases 
      self.atttype = 'slashed'

      self.armour = {'head': armour['head']['none'],
                     'torso': armour['torso']['byte shirt'],
                     'legs': armour['legs']['byte pants'],
                     'feet': armour['feet']['none'],
                     'hands': armour['hands']['none']}

      self.resistance  = self.armour['head']['armour'] + self.armour['torso']['armour'] + self.armour['legs']['armour']\
                         + self.armour['feet']['armour'] + self.armour['hands']['armour']

      
      self.inventory = []

      self.weapon = 'technoblade'

      
   def getHurt(self, damage):
      self.hp -= damage
      if self.hp <= 0:
         return '{} received {} crushing damage and has died!! But fortunately you were dragged to safety.' .format(self.name, damage)
      else:
         return '{} received {} crushing damage!' .format(self.name, damage)
   

   def winBattle(self):
      xpGain = random.randint(100, 300)
      self.xp += xpGain
      print( '{} won the battle and gained {} experience!' .format(self.name, xpGain))
      if self.xp >= self.level_cost[self.level+1]:
         return player().levelUp()


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
      return 'Congradulations!! {} has just leveled up!! Good work.' .format(self.name)


   def displayInv(self):
      for i in self.inventory:
         print(i)
      

   def __str__(self):
      return '''
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

      self.xp = 10
      self.bit = random.randint(5, 20)





class battle:
   def fight(self, a, d):
      while a.hp > 0 and d.hp > 0:
         print('{}: {}' .format(a.name, a.hp))
         print('{}: {}' .format(d.name, d.hp))
         
         battle().turn(a, d, 'slash')
         battle().turn(d, a, 'smash')
         print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
         input('<press enter to continue>')

      else:
         if a.hp <= 0 and d.hp <= 0:
            print('{} and {} have died from their numerous wounds.' .format(a.name, d.name))

         elif a.hp <= 0:
            print('{} has been killed.' .format(a.name))

         elif d.hp <= 0:
            print('{} has been killed.' .format(d.name))
            a.bit += d.bit
            a.xp += d.xp

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
         print('{} {} {} for {} {} damage!!!!' .format(a.name, a.atttype, d.name, damagetype, damagedealt))
         d.hp -= damagedealt

      else:
         print('{} missed!' .format(a.name))


class technovillage:
   def signpost(self):
      print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
      print('You find yourself at a sign post at the center of Technovillage. Where\'d you like to go?')
      print('Places to go: "s"tore, "f"ileinn, "t"rashbin')

      nav = input('^&: ')
      if nav == "s":
         return technovillage().downloadstore()

      elif nav == "f":
         return technovillage().fileinn()

      elif nav == "t":
         return technovillage().trashbin()

      else:
         return technovillage().signpost()
         
   
   def fileinn(self):
      # You can rest and restore your hp here
      price = 10 + 0.1*dp.level
      print('"Good reboot to you! Fileinn at your service! We\'ve got the most comfortable beds in all Computa!"')
      print('"Would you like a room? It only costs {} bits and all your hp gets recovered."' .format(price))
      print('You can type "yes" to sleep or "no" to leave.')
      action = input('Answer:')

      if action == 'yes':
         if dp.bit >= price:
            print('You sleep in an extremely comfortable bed and wake up bright and early the next day.')
            print('"Good reboot! Hope you slept well."')
            input('<*Press ENTER to continue*>')
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
      #This is where you buy and sell items
      print('Hey, welcome to the download store! download any armour you like!')
      for i in armour:
         for x in armour[i]:
            if x == 'none':
               continue
            print('{}: Cost: {}, Armour: {}' .format(armour[i][x]['name'], armour[i][x]['bprice'], armour[i][x]['armour']))

      action = input('What would you like to buy? ')
      print(action)
      for i in armour:
         for x in armour[i]:
            if action == armour[i][x]['name']:
               print('Would you like to buy the {}? ("yes" or "no")' .format(action))
               answer = input('Answer: ')

               if answer == 'yes':
                  if dp.bit >= armour[i][x]['bprice']:
                     print('Sold!')
                     dp.inventory.append(armour[i][x]['name'])
                     return technovillage().downloadstore()
                     print('Item purchased successfully!')
                     input('<*Press ENTER to continue*>')
                  else:
                     print('I\'m sorry but you do not have enough money')
                     return technovillage().downloadstore()
                     input('<*Press ENTER to continue*>')

               elif answer == 'no':
                  return technovillage().downloadstore()
                  input('<*Press ENTER to continue*>')

               elif answer == "leave":
                  return technovillage().signpost()
                  input('<*Press ENTER to continue*>')
                  
            if action == 'leave':
               print('Have a good day!!')
               return technovillage().downloadstore()
               
            #elif not action in armour[i][x]['name']:
               #print('We don\'t have {} here.' .format(action))
               #return technovillage().downloadstore()

      

            
      

   def trashbin(self):
      #Fighting area
      print('Welcome to the trashbin. It\'s endless and you can fight virtually anything.')
      print('We only have viruses here. Do you want to fight the virus?')
      answer = input('Answer: ')

      if answer == 'yes':
         bug = virus()
         battle().fight(dp, bug)
         return technovillage().trashbin


      elif answer == "no":
         return technovillage().signpost()
      
      else:
         return technovillage().trashbin()
      
      

technovillage().signpost()
