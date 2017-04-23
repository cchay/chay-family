class player():
   def __init__(self):
      self.foodPerTurn = 0
      self.woodPerTurn = 0
      self.food = 3
      self.wood = 0
      self.workers = 3
      self.lumbermen = 0
      self.foragers = 0
      self.houses = 0
      self.population = 3
      self.consumption = 3

   def __str__(self):
      return'''
           Town Population: {}
_________________________________________
Workers:      Foragers:     Lumbermen: 
  {}             {}             {}


           Stored Food: {}
_________________________________________
     Food               Food        
  Production:        Consumption:
      {}                  {}


           Stored Wood: {}
_________________________________________
     Wood              Houses
  Production:         Created:
      {}                 {}
'''.format(self.population, self.workers, self.foragers, self.lumbermen, self.food, self.foodPerTurn, self.consumption, self.wood, self.woodPerTurn, self.houses)

player = player()

def create():
   create = input( 'What would you like to create? \
"l", "w", "f"? ' )
   if create == "f" and player.workers > 0:
      player.foragers += 1
      player.workers -= 1
      player.foodPerTurn += 2
   elif create == "l" and player.workers > 0:
      player.lumbermen += 1
      player.woodPerTurn += 1
      player.workers -= 1
   elif create == "w" and player.food > 3:
      player.workers += 1
      player.food -= 3
      player.consumption += 1

def destroy():
   create = input( 'What would you like to destroy? \
"l", "w", "f"? ' )
   if destroy == "f":
      player.foragers -= 1
   elif destroy == "l":
      player.lumbermen -= 1
   elif destroy == "w":
      player.worker -= 1
   consumption -= 1





while player.wood < 50 and player.food < 50:
   player.population = player.workers + player.lumbermen + player.foragers
   player.food -= player.consumption
   player.food += player.foodPerTurn
   player.wood += player.woodPerTurn
   print(player)

   action = input( '\nManage your workers: "c" or "d"\n>' )

   if action == "c":
      create()
      print('\n')
   elif action == "d":
      destroy()
      print('\n')

else:
   if wood >= 50 and food >= 50:
      print( 'You win' )
   
      
      
