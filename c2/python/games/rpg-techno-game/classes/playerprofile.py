import pickle, time, sys

player_profile = pickle.load(open('data/rpg-techno-game-data.pickle', 'rb'))

class player:
   def __init__(self, player_profile, username, password):
      self.name = player_profile[username]['name']
      self.password = password
      self.maxhp = player_profile[username]['maxhp']
      self.hp = player_profile[username]['hp']
      self.level = player_profile[username]['level']
      self.xp = player_profile[username]['xp']
      self.bit = player_profile[username]['bits']
      self.inventory = player_profile[username]['inventory']
      self.wdamage = player_profile[username]['wdamage']

      self.weapon = player_profile[username]['weapon']

      self.level_cost = {2: 10000, #increase based on no algorithum
                         3: 50000,
                         4: 100000,
                         5: 200000,
                         6: 500000}
      
      self.hpinc = {2: 131, # increase of 1.75
                    3: 229,
                    4: 401,
                    5: 702,
                    6: 1228}

      self.attributes = player_profile[username]['attributes']
                        # Player gets 2 skill points per level maybe 1


      self.skills = player_profile[username]['skills']
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

      self.armour = player_profile[username]['armour']

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
   
   
   def winBattle(xp, bit):
      self.xp += xp
      self.bit += bit
      print( '{} received {} exp and {} bits. Good work!' .format(self.name, xp, bit))
      if self.xp >= self.level_cost[self.level+1]:
         return self.levelUp()
      
      player_profile['xp'] = self.xp
      player_profile['bits'] = self.bit
      

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
