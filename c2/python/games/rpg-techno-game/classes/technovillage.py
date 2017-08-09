class technovillage:
   def signpost(self, dp):
      print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
      print('You find yourself at a sign post at the center of Technovillage. Where\'d you like to go?')
      print('Places to go: "as"(armour store), "ws"(weapon store), "am"(armour market, sell armours here), "wm"(weapon market, sell weapons here), "f"ileinn, "t"rashbin, "h"ome, "save" to save the game, or "quit" to exit the game')

      nav = input('^&: ')
      if nav == "as":
         return technovillage().downloadstore_buy(dp)
      
      if nav == "ws":
         return technovillage().buyweapons(dp)

      elif nav == "f":
         return technovillage().fileinn(dp)

      elif nav == "t":
         return technovillage().trashbin(dp)
      
      elif nav == "am":
         return technovillage().downloadstore_sell(armourdata, dp)
      
      elif nav == "wm":
         return technovillage().sellweapons(dp)

      elif nav == "stats":
         print(dp)
         input('<*Press ENTER to continue*>')
         return technovillage().signpost(dp)

      elif nav == "h":
         return technovillage().home(dp)
      
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
         return technovillage().signpost(dp)

      else:
         return technovillage().signpost(dp)
         
   
   def fileinn(self, dp):
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
            technovillage().signpost(dp)
            
            player_profile['bits'] = dp.bit
            player_profile['hp'] = dp.hp
            
         else:
            print('Uhoh, looks like you don\'t have enough bits. Talk to Lena and she will heal you for half price.')
            print('But only if your level is lower than 5.')
            input('<*Press ENTER to continue*>')
            technovillage().signpost(dp)
            
      elif action == "no":
         print('Aww-right, come again soon!!')
         technovillage().signpost(dp)
         
      else:
         return technovillage().fileinn(dp)

   def downloadstore_buy(self, dp):
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
               return technovillage().downloadstore_buy(dp)
            else:
               print('I\'m sorry but you do not have enough money')
               input('<*Press ENTER to continue*>')
               return technovillage().downloadstore_buy(dp)
                           

         elif answer == 'no':
            return technovillage().downloadstore_buy(dp)
            input('<*Press ENTER to continue*>')

         elif answer == "leave":
            print('You leave the armour shop')
            input('<*Press ENTER to continue*>')
            return technovillage().signpost(dp)
                     
      if action == 'leave':
         print('You leave the armour shop')
         input('<*Press ENTER to continue*>')
         return technovillage().signpost(dp)
                     
      if not action in armourlist:
         item = action
         print('We don\'t have {} here.' .format(item))
         return technovillage().downloadstore_buy(dp)

      return technovillage().downloadstore_buy(dp)
   
   
   
   def downloadstore_sell(self, data, dp):
      print('Please select an item in your inventory you would like to sell:')
      for i in dp.inventory:
         print(i)
      item = input('ITEM^^): ')
      if item == "leave":
         return technovillage().signpost(dp)
      
      local = input('Location^^): ')
      
      if item in dp.inventory:
         print('you sell the {} for {} bits.' .format(item, data[local][item]['sprice']))
         dp.bit += data[local][item]['sprice']
         player_profile['bits'] += data[local][item]['sprice']
         player_profile['inventory'].remove(item)
         #dp.inventory.remove(item)
         return technovillage().downloadstore_sell(data, dp)
      
      elif not item in dp.inventory:
         print('I\'m sorry, but you don\'t have {} in your inventory.' .format(item))
         return technovillage().downloadstore_sell(data, dp)
      
      else:
         return technovillage().downloadstore_sell(data, dp)
      
      print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
      
      
      
   def buyweapons(self, dp):
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
               return technovillage().buyweapons(dp)
            else:
               print('I\'m sorry but you do not have enough money')
               input('<*Press ENTER to continue*>')
               return technovillage().buyweapons(dp)
                           

         elif answer == 'no':
            return technovillage().buyweapons(dp)
            input('<*Press ENTER to continue*>')

         elif answer == "leave":
            print('You leave the armour shop')
            input('<*Press ENTER to continue*>')
            return technovillage().signpost(dp)
                     
      if action == 'leave':
         print('You leave the armour shop')
         input('<*Press ENTER to continue*>')
         return technovillage().signpost(dp)
                     
      if not action in weaponlist:
         item = action
         print('We don\'t have {} here.' .format(item))
         return technovillage().buyweapons(dp)

      return technovillage().buyweapons(dp)
   
   
   def sellweapons(self, dp):
      print('Please select a weapon in your inventory you would like to sell:')
      for i in dp.inventory:
         if 'sword' in i:
            print(i)
            
      item = input('ITEM^^): ')
      if item == "leave":
         return technovillage().signpost(dp)
      
      
      if item in dp.inventory:
         print('you sell the {} for {} bits.' .format(item, weapondata[item]['sprice']))
         dp.bit += weapondata[item]['sprice']
         player_profile['bits'] += weapondata[item]['sprice']
         player_profile['inventory'].remove(item)
         #dp.inventory.remove(item)
         return technovillage().sellweapons(dp)
      
      elif not item in dp.inventory:
         print('I\'m sorry, but you don\'t have {} in your inventory.' .format(item))
         return technovillage().sellweapons(dp)
      
      else:
         return technovillage().sellweapons(dp)
      
      print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
      
            
      

   def trashbin(self, dp, bug):
      #Fighting area
      print('Welcome to the trashbin. It\'s endless and you can fight virtually anything.')
      print('We only have viruses here. Do you want to fight the virus?')
      answer = input('Answer: ')

      if answer == 'yes':
         virus = bug
         battle().fight(dp, virus)
         return technovillage().trashbin(dp)

      elif answer == 'maybe':
         virus = bug
         battle().fight(dp, virus)
         return technovillage().trashbin(dp)


      elif answer == "no":
         return technovillage().signpost(dp)
      
      else:
         return technovillage().trashbin(dp)


   def home(self, dp):
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
            return technovillage().home(dp)

         elif action == "ea":
            armour = input('What would you like to equip?')
            local = input('Where? ')
            dp.equipArmour(local, armour)
            print('You equip the {} on your {}' .format(armour, local))
            input('<Press enter to continue>')
            return technovillage().home(dp)
         
         elif action == "ew":
            weapon = input('What weapon would you like to equip?')
            dp.equipWeapon(weapon)
            print('You equip the {}' .format(weapon))
            input('press <ENTER> to continue')
            return technovillage().home(dp)
         
         elif action == "uw":
            weapon = input('What weapon would you like to unequip?')
            dp.unequipWeapon(weapon)
            print('You unequip the {}' .format(weapon))
            input('press <ENTER> to continue')
            return technovillage().home(dp)

         elif action == "v":
		      #print(dp.inventory)
		      #print()
		      #print(dp.armour)

            print('\nInventory:\n')

            for i in dp.inventory:
               print(i)#['name'])
            input('<Press enter to continue>')

            return technovillage().home(dp)

         elif action == "b":
            return technovillage().signpost(dp)

         elif action == "c":
            print(dp)
            input('<Press enter to continue>')
            return technovillage().home(dp)
         
         elif action == "save":
            with open('rpg-techno-game-data.pickle', 'wb') as h:
               pickle.dump(player_profile, h) 
            print('Saving...')
            input('Saved. :)')
            return technovillage().home(dp)

         else:
            input('<Press enter to continue>')
            return technovillage().home(dp)
		
      except KeyError as e:
         #print('There was a key error, try to type the item or location properly next time.. :(')
         return technovillage().home(dp)

