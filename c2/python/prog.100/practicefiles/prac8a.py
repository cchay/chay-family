## This is for Lesson 8
import prac8b

print( 'This is an exponent program.' )

try:
   
   base = input( 'Please enter the integer base value : ' )
   exponent = input( 'Please enter the integer exponent value: ' )

   prac8b.exp( int(base), int(exponent) )
## Up above I had a string problem. I just had to convert it to an integer to process it.

   prac8b.printFib(23)

   fibSeries = prac8b.calcFib(23)
   print (fibSeries)
   
except ValueError as e:
   print( 'You did not enter an integer.' )
