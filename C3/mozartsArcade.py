import time

print('My name is Von Herrn Wolfgang Amadeus Mozart. What is yours?')
name = input()
print(name,', welcome to \'Mozart\'s Arcade\'. Currently, we only have 6 arcade boxes ready for gamers, for the programmers and engineers are but poorly trained, and we have not the funds to train them.. One of them, however, is an educational game.')
print('Please. Choose a game to play.')
time.sleep(5)
print('''You look at a rather scanty list of games:
               Z
               Adventure
               Yourchoice
               Addition
               Hello World Anime
               Triple Game
(please enter the name of the game just the way it is written.)''')

game = input()
if game == "Z":
   import random
   import time
   import sys

   name = input('"Welcome to Survive or Die! I am Byrr Axelus, your host. Please type your name."')
   print(name + ' ,you are about to be faced by a horde of...Guess what?')
   print('"zombies", "aliens", "cannibals"')
   ok = input()
   if ok == "zombies":
      print('That\'s right,' + name + '. A horde of zombies.')
   else:
      print('Not quite,' + name + '. It\'s a horde of zombies. That will be interesting, though.')
   
   print('Your job is to survive and turn as many zombie\'s back to human\'s. You will only be provided with a wooden baseball bat, recently purchased at the sport\'s shop. You must find the rest on your own. If you get bitten, it\'s game over.  Good luck.')
   time.sleep(2)
   print('You see a shop with a sign reading\'Zombie Shop\'. Do you walk in, or walk on?')
   print('"enter" , "walk on"')

   ok = input()
   if ok == "enter":
      print('You walk in, only to hear a loud alarm go off. Do you run out, or stay in?')
      print('"run out","stay in"')

      ok = input()
      if ok == "run out":
         print('You run out of the building, only to be faced by a crowd of zombies. You are almost immediately pulled into the building by a girl of 17. She is armed with a Roughcut 2X4. Seriously? A large man armed with a Mini-Gun emerges from behind the counter. He turns off the alarm.')
      else:
         print('Suddenly, a large man armed with a Mini-Gun emerges from behind the counter. He turns off the alarm. A girl leaps from a back door. She is armed with a Roughcut 2X4.')
         print('The man looks at you."You okay?" he asks. You nod.')
         print('"Have you been infected?" the girl asks, looking you over.')
         print('"What\'s your name?" the man asks.')
         print('You introduce yourself to the others.')
         print('Well, ',name,', you got real lucky back there.You would\'ve been bitten and infected.')
         print('All the while, a boy and another girl barricade the door with an empty shelf and a large, heavy box.')
         print('"My name\'s Bob," the  man continues."That boy\'s Douglass. The girl that saved you is Gail, and the other is Verna. Choose a gun."')
         print('"Hammershot","Roughcut 2x4","Strong Arm"')
   ## Verna has a Roughcut 2X4
   ## Bob has a Mini-Gun
   ## Gail has a Maverick
   ## Douglass has a broken Rampage

   else:
      print('You walk on down the road. Suddenly, a pungent odor fills your lungs, making you gag. A crowd of un-deads surround you. One rather ugly one(who is uglier than the rest)bites you on the shoulder. With a scream of pain, you fall. Then you stand to join the zombie forces.')
      sys.exit()

   nerfgun = input()
   if nerfgun == "Hammershot":
      print('You take the 5 shot "revolver", and chuck the bat.')
   elif nerfgun == "Roughcut 2x4":
      print('You lift the pump action, and chuck the bat.')
   elif nerfgun == "Strong Arm":
      print('You pick up the weighty pistol ,and chuck the bat.')
    
   print('"But really! Why all these____toys?"')
   print('"They are the only effective weapons," Gail states. She is armed with a Maverick. Cool.')
   print('Douglass has a broken Rampage."It will be replaced soon," he said, brushing off some dirt.')
   print('"Let\'s go out and save the world!" Douglass shouts. Everyone laughs.')
   print('"Seriously. What should we do?" Verna states. They all start talking...<Press "enter" to continue>')
   input()
   print('==========================================================================================================')
   print('You finally decide to face the smelly \'green eyes\' as Gail named them. We loaded into an old 4x4 and drive along a trail through the woods.')
   print('"This was used by survivors of the first attack," Douglass informs you.')
   print('"There was another attack?" you ask. Gail nodded. "It was 2 years ago."<Press "enter" to continue>')
   input()
   print('==========================================================================================================')
   print('You yawn and look around. You see Gail scrunched up in the left-hand corner, sleeping soundly. Douglass, curled up to your right, is also sleeping. Bob and Verna are outside the truck, walking out of an abandoned gas station.<Press "enter" to continue>')
   input()
   print('Verna looks at you. "Slept well?" she asks. You nod. She shows you their loot: a hatchet, 12 cans of pork and beans, a machete, and 1,000 Nerf darts. You grin.')
   print('"What\'s up?" Douglass asks. Verna says,"Oh, nothing much."<Press "enter" to continue>')
   input()
   print('Gail continues to sleep like a baby. You and the rest refrain from laughter.')
   print('Bob assigns you to go out with Gail to go and explore the supposedly abandoned neighborhood.')
   print('You go out with Gail to the pitch black neighborhood. A repulsive stench fills your nostrils. Suddenly, a 6\' 9" zombie comes from behind you.')
   print('To be continued...')
elif game == "Adventure":
   import time
   import sys

   print('You find yourself in a tavern, right on the border separating the fields of corn and the wild forest. Before you is a young man, who seems to be about 20 years old.')
   print('"I am Blastemin Stroeger, your host. Please give me your name."')

   name = input()
   print('"Hello,' + name + '.You may choose a short range weapon. Please choose."')

   weapon = input()

   print('"Are you sure you want a',weapon,'? Choose an answer."')
   print('"yes",  "no"')

   ok = input()
   if ok =="yes":
      print('"Alright.We soon will begin the adventure." Blastemin is armed with a bow and a quiver of arrows.')
   else:
      print('"Too bad!"')

   print('"We will be faced by GMO projects, zombies, and mutated living organisms. Maybe a few groups of trolls or gnomes. Let\'s go."<Press \"enter\" to continue.>')
   input()
   print('========================================================================')
   print('You walk through the woods with your host. Suddenly, 14 green gremlins march across your path."We should fight \'em!" Blastemin says. What do you do?')
   print('"attack", "run"')

   ok = input()
   if ok =="attack":
      print('The battle rages furiously. Blastemin climbs a tree. You dart in and out between the trees and rocks, keeping close to Blastemin\'s tree. Blastemin shoots down all the green monsters. You find 3 bronze daggers, 8  iron short swords, and 3 sickles. "Nice fighting, ' + name + '!" Blastemin says.')
      print('You continue the adventure.')
   else:
      print('You run for safety. 7 of the little monsters run after you. Yet, thanks to Blastemin\'s strategy, you manage to win.')
      print('========================================================================')    

   print('Soon, your feet and arm\'s ache.  It put\'s you in a grumpy mood.')
   print('"Let\'s set up camp," Blastemin says. You cook some meat over the blazing fire. You then negotiate who will guard the camp first.')
   print('"I tell you," he laughs. "I will guard the camp first, then you can take shift."')
   print("I will guard first.", " Okay. Good night.")

   ok = input()
   if ok == "I will guard first.":
      print('"If you insist." Blastemin smiles before disappearing into his already-made tent.')
      print('Seconds later, you are attacked by a large UWO(Unidentified Walking Object). You scarcely get out alive.')
      print('========================================================================')    
   else:
      print('You walk into your tent, then fall asleep. You here a loud crashing noise outside. You quickly leap jump from your sleep and look around. You find Blastemin standing over a dead zombie.')
      print('You both take a visit to the land of Nod.')
   print('========================================================================')
   input()
   print('The next morning, you and Blastemin remake the fire.  You go out to hunt and return successful. You pack up the tent\'s, and head on.')
   print('You encounter a black troll, no taller than 2 feet. Do you attack it or talk to it?')
   print('"attack"', '"talk to it"')
   
   ok = input()
   if ok == "attack":   
                        print('You jump at the troll, and quickly kill it. The troll shrieks before falling dead. Other trolls, most likely in waiting, run away in fright. Blastemin looks at you and nods.')
   else:
                        print('"Hi.  I-" you start. But the troll whips out a butterfly knife, stabs you in a blink of an eye, then whistles.  You collapse to the ground, gasping. More trolls leap from the trees, and fight Blastemin. The last thing you see is Blastemin being swarmed by more trolls...')
                        sys.exit()

   print('You are soon tired of the expedition."Don\'t worry. We\'ll find some one,"Blastemin says. You are unsure.')
   print('Very soon, you find a 17 year old girl stumbling through the woods.')
   print('"Need help?" Blastemin asks. "I would like to join you," she says. You later find out that her name is Verna Bogilma.')
   print('<Press "enter" to continue.>')
   input()
   print('Verna pulled a machete out from her bag. She cleaned the blade. Verna evenly distributed 3 cans of Spam, 6 cans of pork and beans, and about 16 oz. of cold coffee(heavily diluted).')
   print('The next morning, you wonder what you do. "We should go south to avoid the brunt," Verna says. "But that\'s the exciting part!" Blastemin exclaims. Who do you agree with?')
   print('"Verna","Blastemin"')
      
   choice = input()
   if choice == "Verna":
      print('"I agree with Verna," you say. Blastemin looks at you. "I guess I\'ll have to go," he finally says.')
      print('You make your way through the thick woods and over ravines. Suddenly, a large ravine opens under you. You, Verna and Blastemin screamed as you fall.')
      print('CRASH! CRUNCH! SMASH!')
      sys.exit()
   else:
      print('"I agree with Blastemin," you say. Verna looks at you. "Count me in," she slowly says.')
      print('You march in the direction of the the busy city. Most of the buildings are smashed or burnt, but few remain standing.')

   print('You clean out your',weapon,', then put it back.')
   print('Verna shows you a newspaper strip.Some parts are blotted. It reads as follows:')
   print('''New monsters "designed" by the Potwells Institution of Technology(PIT). These creatures were called Hu(blotted).
         These new creatures are now on the loose, able to smash through buildings. They have the amazing abilit(blotted)ic
         the human behavior, look, and voice almost perfectly. Only those that have exceedingly sharp ears and eyes will be able to
         pick them out from the crowds.(rest is blotted)
      ''')
   print('Verna looks at you. Her eyes are as round as saucers. You look at her, then at Blastemin. ')
   print('Blastemin reads the strip."Interesting," he murmured. He suddenly looked up. "This means trouble,"')
   print('"What else would it mean?" Verna says. She is still upset that she had to go north instead of south. <Press enter to continue.>')
   input()
   print('Suddenly, an old man hobbles over. "I need help!" Do help him or flee him?')
   print('"help","flee"')
   
   ok = input()
   if ok == "help":
      print('"Oh thank you!" the man cries. His name, you finally find out, is Homerd Vovoglia.')
   else:
      print('You run away from the man. You hear him scream, then silence. You run back to see a zombie.')
      time.sleep(12)
      print('You struggle to run away, but are overrun by a multitude of walking decayed matter.')
      sys.exit()
   print('The man was armed with a lever action, but lacked the ammunition')
   print('To be continued...')
elif game == "Yourchoice":
   import random
   import time

   print('Choose a character.')
   print('"Joe","Bucky","Tim","Brian"')

   ok = input()
   if ok == "Bucky":
         time.sleep(2)
         print('Bucky, you have been hit for 100 points by Joe, and 120 points by Brian!')
         print('YOU HAVE EXPIRED, AND YOU HAVE LOST THE CONTEST OF CHAMPIONS!!!')
   elif ok == "Tim":
         time.sleep(2)
         print('Tim, you are a coward and run for safety from Joe and Brian!')
         print('YOU HAVE FLED, AND YOU HAVE LOST THE CONTEST OF CHAMPIONS!!!')
   elif ok == "Joe":
         time.sleep(2)
         print('Joe, you have hit Bucky for 100 points, chase Tim away, but are easily beaten by Brian!')
         print('YOU HAVE BEEN DEFEATED, AND YOU HAVE LOST THE CONTEST OF CHAMPIONS!!!')
   elif ok == "Brian":
      print('Brian, you hit Joe, Tim, and Bucky for 1,000 points each.')
      print('BRIAN, YOU HAVE WON THE CONTEST OF CHAMPIONS!')
      print('CONGRATULATIONS, UNDEFEATED CHAMPION!!! YOU HAVE WON $1,000,000,000,000!!!')
elif game == "Addition":
   import random

   number1 = random.randint(1, 1000)
   number2 = random.randint(1, 1000)
   print('What is ' + str(number1) + ' + ' + str(number2) + '?')
   answer = input()
   if int(answer) == number1 + number2:
      print('Correct!')
   else:
      print('Nope! The answer is  ' + str(number1 + number2))

elif game == "Hello World Anime":
        import random, sys, time, math, pygame
        from pygame.locals import *

        #set up pygame
        pygame.init()

        #set up window
        windowSurface = pygame.display.set_mode((500, 400), 0, 32)
        pygame.display.set_caption('Hello World!')

        #set up colors
        BLACK = (0, 0, 0)
        WHITE = (225, 225, 225)
        RED = (225, 0, 0)
        GREEN = (0, 225, 0)
        BLUE = (0, 0, 225)

        #set up fonts
        basicFont = pygame.font.SysFont(None, 48)

        #set up the text
        text = basicFont.render('Hello World!', True, WHITE, BLUE)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery

        #draw the white background onto the surface
        windowSurface.fill(WHITE)

        #draw a green polygon onto the surface
        pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291,106), (236, 277), (56, 277), (0, 106)))
        
        #draw some blue lines onto the surface
        pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
        pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
        pygame.draw.line(windowSurface, BLUE, (60,120), (120, 120), 4)

        #draw a blue circle onto the surface
        pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

        #draw a red ellipse onto the surface
        pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

        #draw the text's background rectangle onto the surface
        pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.bottom - 20, textRect.width + 40, textRect.height + 40))

        #get a pixel array of the surface
        pixArray = pygame.PixelArray(windowSurface)
        pixArray[480][380] = BLACK
        del pixArray

        #draw the text onto the surface
        windowSurface.blit(text, textRect)

        #draw the window onto the surface
        pygame.display.update()

        #run the game loop
        while True:
            for event in pygame.event.get():
                if event.type ==QUIT:
                    pygame.quit()
                    sys.exit()

elif game == "Triple Game":
        print('''Type one of the game names below:
adventure
z
yourchoice
(type the names just the way you see it)
''')

game = input()
if game == "adventure":
            import time
            import sys

            print('You find yourself in a tavern, right on the border separating the fields of corn and the wild forest. Before you is a young man, who seems to be about 20 years old.')
            print('"I am Axellis Byrris, your host. Please give me your name."')

            name = input()
            print('"Hello, ' + name + '.You may choose a short range weapon. Please choose."')

            weapon = input()

            print('"Are you sure you want a ',weapon,'? Choose an answer."')
            print('"yes",  "no"')

            ok = input()
            if ok =="yes":
                print('"Alright.We soon will begin the adventure." Axellis is armed with a bow and a quiver of arrows.')
            else:
                print('"Too bad!"')

            print('"We will be faced by GMO projects, zombies, and mutated living organisms. Maybe a few groups of trolls or gnomes. Let\'s go."<Press \"enter\" to continue.>')
            input()
            print('========================================================================')
            print('You walk through the woods with your host. Suddenly, 14 green gremlins march across your path."We should fight \'em!" Axellis says. What do you do?')
            print('"attack", "run"')

            ok = input()
            if ok =="attack":
                print('The battle rages furiously. Axellis climbs a tree. You dart in and out between the trees and rocks, keeping close to Axellis\'s tree. Axellis shoots down all the green monsters. You find 3 bronze daggers, 8  iron short swords, and 3 sickles. "Nice fighting, ' + name + '!" Axellis says.')
                print('You continue the adventure.')
            else:
                print('You run for safety. 7 of the little monsters run after you. Yet, thanks to Axellis\'s strategy, you manage to win.')
                print('========================================================================')    

            print('Soon, your feet and arm\'s ache.  It put\'s you in a grumpy mood.')
            print('"Let\'s set up camp," Axellis says. You cook some meat over the blazing fire. You then negotiate who will guard the camp first.')
            print('"I tell you," he laughs. "I will guard the camp first, then you can take shift."')
            print("I will guard first.", " Okay. Good night.")

            ok = input()
            if ok == "I will guard first.":
                print('"If you insist." Axellis smiles before disappearing into his already-made tent.')
                print('Seconds later, you are attacked by a large UWO(Unidentified Walking Object). You scarcely get out alive.')
                print('========================================================================')    
            else:
                print('You walk into your tent, then fall asleep. You here a loud crashing noise outside. You quickly leap jump from your sleep and look around. You find Axellis standing over a dead zombie.')
                print('You both take a visit to the land of Nod.')
            print('========================================================================')
            input()
            print('The next morning, you and Axellis remake the fire.  You go out to hunt and return successful. You pack up the tent\'s, and head on.')
            print('You encounter a black troll, no taller than 2 feet. Do you attack it or talk to it?')
            print('"attack"', '"talk to it"')

            ok = input()
            if ok == "attack":   
               print('You jump at the troll, and quickly kill it. The troll shrieks before falling dead. Other trolls, most likely in waiting, run away in fright. Axellis looks at you and nods.')

            else:
                print('"Hi.  I-" you start. But the troll whips out a butterfly knife, stabs you in a blink of an eye, then whistles.  You collapse to the ground, gasping. More trolls leap from the trees, and fight Axellis. The last thing you see is Axellis being swarmed by more trolls.........')
                sys.exit()

            print('You are soon tired of the expedition."Don\'t worry. We\'ll find some one,"Axellis says. You are unsure.')
            print('Very soon, you find a 17 year old girl stumbling through the woods.')
            print('"Need help?" Axellis asks. "I would like to join you," she says. You later find out that her name is Verna Bogilma.')
            print('<Press "enter" to continue.>')
            input()
            print('Verna pulled a machete out from her bag. She cleaned the blade. Verna evenly distributed 3 cans of Spam, 6 cans of pork and beans, and about 16 oz. of cold coffee(heavily diluted).')
            print('The next morning, you wonder what you do. "We should go south to avoid the brunt," Verna says. "But that\'s the exciting part!" Axellis exclaims. Who do you agree with?')
            print('"Verna","Axellis"')

            choice = input()
            if choice == "Verna":
                print('"I agree with Verna," you say. Axellis looks at you. "I guess I have to go," he finally says.')
                print('You make your way through the thick woods and over ravines. Suddenly, a large ravine opens under you. You, Verna and Axellis screamed as you fall.')
                print('CRASH! CRUNCH! SMASH!')
                print('''                     _      _
                       ______________     1   1    ______________
                                            1    1   1    1
                                            1      \ /      1
                                            1      1  V   1
                                            1      1       1
                                            1     /1\      1
                                            1    1 0 1   1
                                            1               1
                                            1               1
                                            1    1   1    1
                                            1    1   1    1
                                            1     \ /       1
                                            1      1       1
                                            1      1  A   1
                                            1     /1\      1
                                            1   1 0 1    1                                         
                                            1               1
                                            1               1
                                            1   _     _    1
                                            1    1   1    1
                                            1    1   1    1
                                            1     \ /       1
                                            1      1   Y  1
                                            1      1       1
                                            1     /1\      1
                                            1   1 0 1    1
                                            1_________ 1
                ''')
                sys.exit()
            else:
                print('"I agree with Axellis," you say. Verna looks at you. "Count me in," she slowly says.')
                print('You march in the direction of the the busy city. Most of the buildings are smashed or burnt, but few remain standing.')

            print('You clean out your',weapon,', then put it back.')
            print('Verna shows you a newspaper strip.Some parts are blotted. It reads as follows:')
            print('''New monsters "designed" by the Potwells Institution of Technology(PIT). These creatures were called Hu(blotted).
    These new creatures are now on the loose, able to smash through buildings. They have the amazing abilit(blotted)ic
    the human behavior, look, and voice almost perfectly. Only those that have exceedingly sharp ears and eyes will be able to
    pick them out from the crowds.(rest is blotted)
         ''')
            print('Verna looks at you. Her eyes are as round as saucers. You look at her, then at Axellis. ')
            print('Axellis reads the strip."Interesting," he murmured. He suddenly looked up. "This means trouble,"')
            print('"What else would it mean?" Verna says. She is still upset that she had to go north instead of south. <Press enter to continue.>')
            input()
            print('Suddenly, an old man hobbles over. "I need help!" Do help him or flee him?')
            print('"help","flee"')

            ok = input()
            if ok == "help":
                print('"Oh thank you!" the man cries. His name, you finally find out, is Howard Vovoglia.')
            else:
                print('You run away from the man. You hear him scream, then silence. You run back to see a zombie.')
elif game == "z":
    import random
    import time
    import sys

    name = input('"Welcome to Survive or Die! I am Byrr Axelus, your host. Please type your name."')
    print(name + ' ,you are about to be faced by a horde of...Guess what?')
    print('"zombies", "aliens", "cannibals"')
    ok = input()
    if ok == "zombies":
        print('That\'s right,' + name + '. A horde of zombies.')
    else:
        print('Not quite,' + name + '. It\'s a horde of zombies. That will be interesting, though.')

    print('Your job is to survive and turn as many zombie\'s back to human\'s. You will only be provided with a wooden baseball bat, recently purchased at the sport\'s shop. You must find the rest on your own. If you get bitten, it\'s game over.  Good luck.')
    time.sleep(2)
    print('You see a shop with a sign reading\'Zombie Shop\'. Do you walk in, or walk on?')
    print('"enter" , "walk on"')

    ok = input()
    if ok == "enter":
        print('You walk in, only to hear a loud alarm go off. Do you run out, or stay in?')
        print('"run out","stay in"')
    else:
        print('You walk on down the road. Suddenly, a pungent odor fills your lungs, making you gag. A crowd of undeads surround you. One rather ugly one(who is uglier than the rest)bites you on the shoulder. With a scream of pain, you fall. Then you stand to join the zombie forces.')
        sys.exit()
    
        ok = input()
        if ok == "run out":
            print('You run out of the building, only to be faced by a crowd of zombies. You are almost immediately pulled into the building by a girl of 17. She is armed with a Roughcut 2X4. Seriously? A large man armed with a Mini-Gun emerges from behind the counter. He turns off the alarm.')
        else:
            print('Suddenly, a large man armed with a Mini-Gun emerges from behind the counter. He turns off the alarm. A girl leaps from a back door. She is armed with a Roughcut 2X4.')
            print('The man looks at you."You okay?" he asks. You nod.')
            print('"Have you been infected?" the girl asks, looking you over.')
            print('"What\'s your name?" the man asks.')
            print('You introduce yourself to the others.')
            print('Well, ',name,', you got real lucky back there.You would\'ve been bitten and infected.')
            print('All the while, a boy and another girl barricade the door with an empty shelf and a large, heavy box.')
            print('"My name\'s Bob," the  man continues."That boy\'s Douglass. The girl that saved you is Gail, and the other is Verna. Choose a gun."')
            print('"Hammershot","Roughcut 2x4","Strong Arm"')
    ## Verna has a Roughcut 2X4
    ## Bob has a Mini-Gun
    ## Gail has a Maverick
    ## Douglass has a broken Rampage

    print('Suddenly, a large man armed with a Mini-Gun emerges from behind the counter. He turns off the alarm. A girl leaps from a back door. She is armed with a Roughcut 2X4.')
    print('The man looks at you."You okay?" he asks. You nod.')
    print('"Have you been infected?" the girl asks, looking you over.')
    print('"What\'s your name?" the man asks.')
    print('You introduce yourself to the others.<Press "Enter" to continue>')
    input()
    print('Well, ',name,', you got real lucky back there.You would\'ve been bitten and infected.')
    print('All the while, a boy and another girl barricade the door with an empty shelf and a large, heavy box.')
    print('"My name\'s Bob," the  man continues."That boy\'s Douglass. The girl that saved you is Gail, and the other is Verna. Choose a gun."')
    print('"Hammershot","Roughcut 2x4","Strong Arm"')

    nerfgun = input()
    if nerfgun == "Hammershot":
        print('You take the 5 shot "revolver", and chuck the bat.')
    elif nerfgun == "Roughcut 2x4":
        print('You lift the pump action, and chuck the bat.')
    elif nerfgun == "Strong Arm":
        print('You pick up the weighty pistol ,and chuck the bat.')
    
    print('"But really! Why all these____toys?"')
    print('"They are the only effective weapons," Gail states. She is armed with a Maverick. Cool.')
    print('Douglass has a broken Rampage."It will be replaced soon," he said, brushing off some dirt.')
    print('"Let\'s go out and save the world!" Douglass shouts. Everyone laughs.')
    print('"Seriously. What should we do?" Verna states. They all start talking...<Press "enter" to continue>')
    input()
    print('==========================================================================================================')
    print('You finally decide to face the smelly \'green eyes\' as Gail named them. We loaded into an old 4x4 and drive along a trail through the woods.')
    print('"This was used by survivors of the first attack," Douglass informs you.')
    print('"There was another attack?" you ask. Gail nodded. "It was 2 years ago."<Press "enter" to continue>')
    input()
    print('==========================================================================================================')
    print('You yawn and look around. You see Gail scrunched up in the left-hand corner, sleeping soundly. Douglass, curled up to your right, is also sleeping. Bob and Verna are outside the truck, walking out of an abandoned gas station.<Press "enter" to continue>')
    input()
    print('Verna looks at you. "Slept well?" she asks. You nod. She shows you their loot: a hatchet, 12 cans of pork and beans, a machete, and 1,000 Nerf darts. You grin.')
    print('"What\'s up?" Douglass asks. Verna says,"Oh, nothing much."<Press "enter" to continue>')
    input()
    print('Gail continues to sleep like a baby. You and the rest refrain from laughter.')
    print('Bob assigns you to go out with Gail to go and explore the supposedly abandoned neighborhood.')
    print('To be continued...')
elif game == "yourchoice":
    import random
    import time

    print('Choose a character.')
    print('"Joe", "Bucky", "Tim", "Brian"')

    ok = input()
    if ok == "Bucky":
        time.sleep(2)
        print('Bucky, you have been hit for 100 points by Joe, and 120 points by Brian!')
        print('YOU HAVE EXPIRED, AND YOU HAVE LOST THE CONTEST OF CHAMPIONS!!!')
    elif ok == "Tim":
        time.sleep(2)
        print('Tim, you are a coward and run for safety from Joe and Brian!')
        print('YOU HAVE FLED, AND YOU HAVE LOST THE CONTEST OF CHAMPIONS!!!')
    elif ok == "Joe":
        time.sleep(2)
        print('Joe, you have hit Bucky for 100 points, chase Tim away, but are easily beaten by Brian!')
        print('YOU HAVE BEEN DEFEATED, AND YOU HAVE LOST THE CONTEST OF CHAMPIONS!!!')
    elif ok == "Brian":
        print('Brian, you hit Joe, Tim, and Bucky for 1,000 points each with your big hard head.')
        print('BRIAN, YOU HAVE WON THE CONTEST OF CHAMPIONS!!')
        print('CONGRATULATIONS, UNDEFEATED CHAMPION!!! YOU HAVE WON $1,000,000,000,000!!!')
