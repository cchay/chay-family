import time

instructions = 'These are the instructions for the game:\n1.Eat to live\n2.Fight to level up\n3.Make friends'

def gameDialog(sentence):
   sentence.split()
   new_sentence = []

   for i in sentence:
      i.split()
      new_sentence.append(i)

   for i in new_sentence:
      print(i, end="")
      time.sleep(0.03)

introduction = ['Long long ago there lived a king in the ancient and remote part of Europe...',
                          '...his name was Asgar Rommel and he heard of the strange place of Havenville...',
                          '...a 25 room dungeon filled with monsters and loot and only the bravest ventured...',
                          '...to the most horrible dungeon in history ...',
                         '...here our story begins...']

for i in introduction:
   gameDialog(i)
   input('^')

#import DungeonRpg_v2
