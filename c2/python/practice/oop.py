import random

class Employee:
   def __init__( self, name, hourlypay ):
      self.name = name
      self.hourlypay = hourlypay
      self.grosspay = self.hourlypay *8*5*52
      self.netpay = self.grosspay - ( self.grosspay * 0.18 )

   def __str__( self ):
      return self.name + " makes $" + str(self.netpay) + " a year."

def job():
   jobs = ["Doctor", "Programmer", "Contracter", "Librarian", "Fire fighter", "EMT"]
   return jobs[ random.randint( 0, 5 ) ]

job = job()
if job == "Doctor":
   hp = random.randint( 150, 250 )
elif job == "Programmer":
   hp = random.randint( 50, 80 )
elif job == "Contracter":
   hp = random.randint( 6, 15 )
elif job == "Librarian":
   hp = random.randint( 8, 15 )
elif job == "Fire fighter":
   hp = random.randint( 40, 60 )
elif job == "EMT":
   hp = random.randint( 20, 40 )

name = input("What is your name?\n")

e1 = Employee( name, hp )
print( e1.name + ', ' + job + ', You make $' + str(hp) + ' an hour.' )
print( e1 )

if e1.netpay > 60000:
   print( 'You make enough money to support yourself.' )
else:
   print( 'You are unable to support yourself.' )













