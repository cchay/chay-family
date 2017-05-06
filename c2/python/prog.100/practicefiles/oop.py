import time, sys, random

class TownCenter():
   def __init__(self):
      self.foodPerTurn = 0
      self.woodPerTurn = 0
      self.food = 0
      self.wood = 0
      self.workers = 3
      self.lumbermen = 0
      self.foragers = 0

   def __str__(self):
      return '''

             Workers:     {0}
             Lumbermen:   {1}
             Foragers:    {2}

             Food:        {3}
             Wood:        {4}

''' .format(tc.workers, tc.lumbermen, tc.foragers, tc.food, tc.wood)

   def destroy(self):
      create = input( 'What would you like to destroy? \
"l", "w", "f"? ' )
   if destroy == "f":
      tc.foragers -= 1
   elif destroy == "l":
      tc.lumbermen -= 1
   elif destroy == "w":
      tc.worker -= 1

   def create(self):
   create = input( 'What would you like to create? \
"l", "w", "f"? ' )
      if create == "f" and tc.workers > 0:
         tc.foragers += 1
         tc.workers -= 1
         tc.foodPerTurn += 1
      elif create == "l" and tc.workers > 0:
         tc.lumbermen += 1
         tc.woodPerTurn += 1
         tc.workers -= 1
      elif create == "w" and tc.food > 3:
         tc.workers += 1
         tc.food -= 3

tc = TownCenter()

while tc.wood < 50 or tc.food < 50:
   tc.food = tc.foodPerTurn + tc.food
   tc.wood = tc.woodPerTurn + tc.wood
   print(tc)
   action = input( 'Manage your workers: "c" or "d" ' )

   if action == "c":
      tc.create()
   elif action == "d":
      tc.destroy()
else:
   if tc.wood >= 50 and tc.food >= 50:
      print( 'You win' )
   
      
      
'''
def printStatus():
   print( status )
   
def create():
   global workers, lumbermen, foragers, foodPerTurn, woodPerTurn, food
   create = input( 'What would you like to create? \
"l", "w", "f"? ' )
   if create == "f" and workers > 0:
      foragers += 1
      workers -= 1
      foodPerTurn += 1
   elif create == "l" and workers > 0:
      lumbermen += 1
      woodPerTurn += 1
      workers -= 1
   elif create == "w" and food > 3:
      workers += 1
      food -= 3

def destroy():
   global workers, lumbermen, foragers
   create = input( 'What would you like to destroy? \
"l", "w", "f"? ' )
   if destroy == "f":
      foragers -= 1
   elif destroy == "l":
      lumbermen -= 1
   elif destroy == "w":
      worker -= 1


foodPerTurn = 0
woodPerTurn = 0

food = 0
wood = 0

workers = 3
lumbermen = 0
foragers = 0

'''
