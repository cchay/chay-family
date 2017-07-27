import time, sys, random

####################################################################################

print('My name is Von Herrn Wolfgang Amadeus Mozart. What is your name?')
name = input()
print(name,', welcome to \'Mozart\'s Arcade\'. Currently, we only have 6 arcade boxes ready for gamers, as we lack the funds for anymore, and we don\'t have a sponser, either. One of them, however, is an educational game. <Press "Enter" to continue>')
input()
print('Please. Choose a game to play. <Press "Enter" to continue>')
input()
print('''You look at a rather scanty list of games:
               Z
               Adventure
               Addition
(please enter the name of the game just the way it is written.)''')



game = input()
if game == "Z":
   import random
   import time
   import sys

   name = input('"Welcome to Zombie Ex-Cursion! I am Greff Hodan, your host. Please type your name."')
   print(name + ' ,you are about to be faced by a horde of...Guess what?')
   print('"zombies", "aliens", "cannibals"')
   mob = input()
   if mob == "zombies":
      print('That\'s right,' + name + '. A horde of zombies.')
   else:
      print('Not quite,' + name + '. It\'s a horde of zombies. That will be interesting, though.')
   
   print('Your job is to survive and turn as many zombie\'s back to human\'s. You will only be provided with a wooden baseball bat, recently purchased at the sport\'s shop. You must find the rest on your own. If you get bitten, it\'s game over.  Good luck.')
   input()
   print('You see a shop with a sign reading "Zombie Shop". Do you walk in, or walk on?')
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

   if ok == "walk on":
      print('You walk on down the road. Suddenly, a pungent odor fills your lungs, making you gag. A crowd of un-deads surround you. One rather ugly one(who is uglier than the rest)bites you on the shoulder. With a scream of pain, you fall. Then you stand to join the zombie forces.')
      sys.exit()

   nerfgun = input()
   if nerfgun == "Hammershot":
      print('You take the 5 shot "revolver", and chuck the bat.')
   elif nerfgun == "Roughcut 2x4":
      print('You lift the pump action, and chuck the bat.')
   elif nerfgun == "Strong Arm":
      print('You pick up the weighty pistol ,and chuck the bat.')
    
   print('"But really! Why all these...toys?"')
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



#####################################################################################3




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



#############################################################################




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



############################################################################
