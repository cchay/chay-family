def exp( x, y ):
   z = x ** y
   print(z)

def printFib( n ):
   a, b = 0, 1
   while b < n:
      print(b)
      a,b = b, a+b

def calcFib( n ):
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a,b = b, a+b  
   return result
def byValExample( x ):
   x = "This value is overridden!"
   print(x)
