## Grade: 90%

import sys

numbers = []
for i in range( 10000, 150, -2 ):
   numbers.append( i )

while True:
   try:
      number = input( 'Type a number less than 10,000 or "0" to exit. ' )
      
      if number == "0":
         sys.exit()
         
      for i in numbers:
         if i % int(number) == 0:
            print( i, 'is evenly divisible by', number )

      if int(number) > 10000:
         print( 'The number you entered was too big.' )
         continue
         
      print()
   except KeyboardInterrupt as e:
      continue
      
