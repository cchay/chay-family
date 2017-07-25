import time, sys, random


###############################################################################


playerHp = 50
playerWeapon = "(none)"
gold = random.randint( 0, 20 )


###############################################################################


print( 'Doctor Taydo: Welcome to the Cybernetic Testing Chamber. What is you name?' )
name = input()

print( 'Doctor Taydo: We are currently looking for a tester for our Project 23:967. Will you be our tester for this years project? (yes/no)' )
choice = input()



print( '''
Name:''',name,'''
Health:''',playerHp,'''
Weapon:''',playerWeapon,'''
Gold:''',gold,'''


<Press "enter" to continue>
''' )

input()



if choice == "yes":
    playerWeapon = "long sword"
    gold = gold + 50
    print( 'Doctor Taydo: Excellent! Here, you\'ll need this.' )
    print( 'You are handed a long sword and a bag of gold.' )
    time.sleep(1)
elif choice == "no":
    print( 'Doctor Taydo: Hmm, that\'s a shame. I was looking forward to sending you to the world, but you, obviously, either aren\'t ready, or you don\'t have the nerve. I will see you another time.' )
    sys.exit()
elif choice != "no" and choice != "yes":
    print( 'Doctor Taydo: Hmm, that\'s a shame. I was looking forward to sending you to the world, but you, obviously, either aren\'t ready, or you don\'t have the nerve. I will see you another time.' )
    sys.exit()






print( 'Doctor Taydo: (points to a large metal cannister) That is the gateway to the virtual world. Please. Step in. <Press "enter" to continue>' )
input()
print( 'You step into the large drum. The door closes with a loud clang. <Press "enter" to continue>' )
input()
print( 'Doctor Taydo: This will only take a moment! Hold fast! <Press "enter" to continue>' )
input()
print( 'You feel a sort of fizzle spread across your body, from your brain to your bones. A knot is tied into your stomach. You black out...<Press "enter" to continue>' )
input()
time.sleep( 2.5 )
print( '...' )
time.sleep( 2.5 )
print( '...' )
time.sleep( 2.5 )
print( '...' )
time.sleep( 2.5 )
print( 'You feel...' )
time.sleep( 2.5 )
print( '...Heavy...' )
time.sleep( 2.5 )
print( '...But also light...' )
time.sleep( 2.5 )
print( '...At the same time...' )
time.sleep( 2.5 )
print( 'You find yourself in a large field, surrounded by the lush green grass and tall trees.' )
print( '''
Name:''',name,'''
Health:''',playerHp,'''
Weapon:''',playerWeapon,'''
Gold:''',gold,'''

''' )
