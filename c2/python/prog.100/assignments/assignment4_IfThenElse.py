## This is a joke program.
## Grade: 100%
import random, sys

## Create a variety of jokes with my own function
joke = [ "What do you get when you cross a Guido Van Rossum with a flying circus? ",
             "What do dentist's call a blackhole? ",
             "What did the lightbulb say to the other lightbulb? ",
             "How do you know if an elephant has been in your house? "]
jokesCorrect = 0
name = input( 'Hi! What is your name? ' )

# Now this will continuously generate jokes.

print()
print( joke[0] )
answer = input( '''"a". Cobra
"b". Flying Rossum
"c". Python
''' )
if answer == "c":
   print( 'Python!!, Correct' )
   jokesCorrect += 1
elif answer == "b":
   print( 'That\'s hillarious!! But not quite, %s.' % name )
else:
   print( 'Nope, not quite.' )

print()
print( joke[2] )
answer = input('''"a". Watt is going on?
"b". Watcha doin' ?
"c". Your bill is overdue!!
''')
if answer == "a":
   print( 'You guessed it!!' )
   jokesCorrect += 1
else:
   print( 'That was pretty close, I assure you.' )

print()
print( joke[3] )
answer = input('''"a". When your roof is gone.
"b". When you have to replace your bed.
"c". When you hear trumpting in the distance.
''')
if answer == "a" or answer == "b":
   print( 'Lol, that\'s right!!' )
   jokesCorrect += 1
else:
   print( 'Sorry, maybe next time.')

print()
print( joke[1] )
answer = input('''"a". A cavity!!
"b". A sign for a root-canal'
"c". Bad breath.
''')
if answer == "a":
   print( 'Correct!!' )
   jokesCorrect += 1
else:
   print( 'You were very close.')

print()
if jokesCorrect == 4:
   print( 'Wow!! %s, you are great at this.' )
   print( 'Your score is %i.' % name, jokesCorrect )
elif jokesCorrect > 1:
   print( 'You did pretty well.' )
   print( 'Your score is %i.' % jokesCorrect )
elif jokesCorrect == 1:
   print( '%s, I think you should get a joke book.' )
   print( 'Your score is %i.' % name, jokesCorrect )
else:
   print( 'I feel really sorry for you, %s' )
   print( 'Your score is %i.' % name, jokesCorrect )








