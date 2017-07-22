## Let's create a pizza making function
# Let's create 3 different types: The Works(My favourite), Cheeze and Pepperoni
from time import sleep

toppings = []

def pizzaMaker(pizzatype, topping):
   print('Selecting ingredients....')
   sleep(1)

   def pepperonipizza(topping):
      topping.append('pepperoni', 'cheeze')

   def workspizza():
      topping.append(['pepperoni', 'cheeze', 'sausages', 'onions', 'olives',
                     'green peppers'])

   def cheezepizza():
      topping.append('cheeze')
   

   if pizzatype == 'pepperoni':
      return pepperonipizza()

   elif pizzatype == 'the works':
      return workspizza()

   elif pizzatype == 'cheeze':
      return cheezepizza()



print('What kind of pizza would you like?')
pizza = input('"pepperoni", "the works" or "cheeze" pizza')

pizzaMaker(pizza, toppings)
print('Baking Pizza...')
sleep(1)

print('\n\n{} pizza:' .format(pizza))
print('\tToppings:')
for i in toppings:
   for j in i:
      print('\t  ', j)

