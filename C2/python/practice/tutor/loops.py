## What are loops?

#while loop: executes code as long as the condition is true

#for loop; iterates over every item in a sequence

hp = 0

while True:
   hp = hp + 1
   print('My health is at', hp)
   if hp == 10:
      break
print('I feel much better')

for i in range(1,11):
   print('My health is at', i)
print('I feel much better')
