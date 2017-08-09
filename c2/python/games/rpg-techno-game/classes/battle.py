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
            a.winBattle(d.xp, d.bit)

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

