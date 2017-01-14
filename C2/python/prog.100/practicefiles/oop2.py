import math, random

def calcCircumference( radius ):
	return math.pi * 2 * radius
	
class Circles:
	pass
	
circles = []

for i in range ( 0, 10 ):
	c = Circle()
	c.radius = random.uniform( 1.1, 9.5 )
	c.circumference = calcCircumference()
	circles.append( i )
	
for c in circles:
	print()
