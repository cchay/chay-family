## Christopher Chay, 2016.1.16
##Assignment 2: Make a list of my family and a dictionary of one memeber(name.age,gender)
## Grade: 110%

import time

name = input("Hi! I'm Peter Mopark. What is your name? ")

age = input("What is your age? ")

gender = input("And finally, What is your gender? ")

   
time.sleep(1)
print("processing...")
time.sleep(1)
persondict = {'Name: ' : name, 'Age: ' : age, 'Gender' : gender }
print('The final results are: ', persondict)

choice = input('Would you like to change anything? (type y or yes) or press enter to continue.')
if choice == "yes" or choice == "y":
   while 1 ==1:
      choice1 = input('''What would you like to change?
name
age
gender
(or type z to quit)
''')
      if choice1 == "name":
         name = input('Please type a new name: ')
         persondict = {'Name: ' : name, 'Age: ' : age, 'Gender' : gender }
         print('The new results are: ', persondict)
      elif choice1 == "age":
         age = input('Please type a new age: ')
         persondict = {'Name: ' : name, 'Age: ' : age, 'Gender' : gender }
         print('The new results are: ', persondict)
      elif choice1 == "gender":
         gender = input('Please type a new gender: ')
         persondict = {'Name: ' : name, 'Age: ' : age, 'Gender' : gender }
         print('The new results are: ', persondict)
      elif choice1 == "z":
         break
else:
   pass

persondict = {'Name: ' : name, 'Age: ' : age, 'Gender' : gender }
print('The final results are: ', persondict)
