import time, sys, random


###############################################################################


playerHp = 50
weapon = "(fists)"
gold = random.randint( 0, 20 )


###############################################################################


daggerp = 1
shortswordp = 10
longswordp = 50
axep = 150
spearp = 200
halberdp = 500
greatswordp = 2000


###############################################################################


monsterHp = 25



###############################################################################


print( 'Doctor Taydo: Welcome to the Cybernetic Testing Chamber. What is your name?' )
name = input()

print( 'Doctor Taydo: We are currently looking for a tester for our Project RB:34. Will you be our tester for this years project? (yes/no)' )
choice = input()



print( '''
Name:''',name,'''
Health:''',playerHp,'''
Weapon:''',weapon,'''
Gold:''',gold,'''


<Press "enter" to continue>
''' )

input()



if choice == "yes":
    weapon = "long sword"
    gold = gold + 50
    print( 'Doctor Taydo: Excellent! Here, you\'ll need this.' )
    print( 'You are handed a long sword and a bag of gold. <Press "enter" to continue>' )
    input()
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
print( '... <Press "enter" to continue>' )
input()
print( '...' )
input()
print( '...' )
input()
print( 'You feel...' )
input()
print( '...Heavy...' )
input()
print( '...But also light...' )
input()
print( '...At the same time.' )
input()
print( 'You find yourself in a large field, surrounded by the lush green grass and tall trees. <Press "enter" to continue>' )
input()
print( '''
Name:''',name,'''
Health:''',playerHp,'''
Weapon:''',weapon,'''
Gold:''',gold,'''

''' )


input()


print( 'While you are busy enjoying the fresh air of the outside, you hear a twig snap.  <Press "enter" to continue>' )
input()
print( 'You whip around and a small fox comes into view. You have no other choice, but to engage.' )

input()

print( 'You: Down with you, you pesky little fox!' )
print( 'You ready your',weapon,'and prepare yourself for battle.' )

while playerHp > 0 and monsterHp > 0:
    if weapon == "fists":
                p1Damage = random.randint( 0, 5 )
    if weapon != "fists":
                p1Damage = random.randint( 0, 10 )
    monDamage = random.randint( 0, 3 )
    monsterHp = monsterHp - p1Damage
    playerHp = playerHp - monDamage
    print( 'You swing your',weapon,'at the fox, causing',p1Damage,'damage!' )
    print( 'Fox bites you, causing',monDamage,'damage!' )
    print( name,'   Health:',playerHp, '    Weapon:',weapon )
    print( 'Fox   Health:',monsterHp, '    Weapon: teeth ' )
    input( '<Press "enter" to continue.>' )
    print( '=========================================' )

    if playerHp <= 0:
        print( 'Too bad, you died.' )
        sys.exit()

    if monsterHp <= 0:
        gold = gold + gold
        print( 'Congratulations! you have won against the fox! you recieve',gold,'gold!!' )
        print( '''
Name:''',name,'''
Health:''',playerHp,'''
Weapon:''',weapon,'''
Gold:''',gold,'''

''' )
        break


print( '''You arrive at a small village. You can visit one place for now. Please choose:
Weapons Shop
Armour Shop
Healing''' )

dest = input()

if dest == "Healing":
    print( '"Welcome to the Healing house. A drink from our fountain will restore your health, but at a cost. It is 5 gold. Would you like a drink?"' )
    heal = input()
    if heal == "yes":
        playerHp = 50
        gold = gold - 5
        print( 'Health restored.' )
        print( 'Gold:',gold )


if dest == "Weapons Shop":
    print( 'Welcome to the weapon shop! What would you like today?' )
    print( gold )
    print( '''
dagger     1gp
short sword     10gp
long sword     50gp
axe     150gp
spear    200gp
halberd    500gp
great sword    2 000gp
''' )
    purchase = input()
    if purchase == "dagger":
        gold = gold - daggerp
        print( 'You have sucessfully purchased a',purchase )
    if purchase == "short sword":
        gold = gold - shortswordp
        print( 'You have sucessfully purchased a',purchase )
    if purchase == "long sword":
        gold = gold - longswordp
        print( 'You have sucessfully purchased a',purchase )
    if purchase == "axe":
        gold = gold - axep
        print( 'You have sucessfully purchased a',purchase )
    if purchase == "spear":
        gold = gold - spearp
        print( 'You have sucessfully purchased a',purchase )
    if purchase == "halberd":
        gold = gold - halberdp
        print( 'You have sucessfully purchased a',purchase )
    if purchase == "great sword":
        gold = gold - greatswordp
        print( 'You have sucessfully purchased a',purchase )

if gold <= 0:
    print( 'You\'re in biiiiiig trouble, buster.' )


print( 'This is still work in progress. Stay tuned for more!' )
