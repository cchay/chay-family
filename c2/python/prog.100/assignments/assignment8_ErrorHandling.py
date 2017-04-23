# Christopher Chay
# 2016.3.31
# Assignment 8: Error Handling
# Grade: ---

def createSuper( x, y, z, a ):
   x, y, z, a = x, y, z, a
   return 'Superhero: ' + str(x) + '\n' + \
            'Secret Identity: ' + str(y) + '\n' + \
            'Age: ' + str(z) + '\n' + \
            'Powers: ' + int(a)
   

try:
   super1 = createSuper( 'Spider Man', 'Peter Parker', 20, 'Wall crawling, super strength, agility, web' )
   super2 = createSuper( 'Captain America', 'Steve Rogers', 18, 'Super strength, Super-high Endurance, Super-speed' )
   super3 = createSuper( 'Super Man', 'Clark Kent', 32, 'Super strength, Flight, Laser-vision, Heat-Vision, Icy-Breath' )

except ValueError as e:
   print( '\nError Message:', e, '\n' )
except TypeError as e:
   print( '\nError Message:', e, '\n' )
except AttributeError as e:
   print( '\nError Message:', e, '\n' )
except NameError as e:
   print( '\nError Message:', e, '\n' )
else:
   print( str(super1) + '\n\n' + str(super2) + '\n\n' + str(super3) )  
   

     
