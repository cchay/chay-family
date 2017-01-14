import random

def make_an_omelet( omelet_type ):
   omelet = ''
   def everything():
      omelet = 'eggs, salt, mushroom, pepper, swiss cheese, ham'
      omelet = 'Your omelet costs {} dollars.' .format(random.randint(1, 6))
      return omelet
   def cheese():
      omelet = 'eggs, salt, swiss cheese, american cheese'
      omelet = 'Your omelet costs {} dollars.' .format(random.randint(1, 4))
      return omelet

   if omelet_type == "everything":
      omelet = everything()
      return omelet

   elif omelet_type == "cheese":
      omelet = cheese()
      return omelet
