#I'm going to create a story based RPG text adventure game. You need to have certain stats to survive certai choices or you die. Whatever choices you make will depends on you, and the stats you choose to increase.

import sys

class player:
   def __init__(self, name):
      self.name = name
      
      # Combat Stats: 
      # Speed, combat, strength, hearing, observation, 
      
      self.speed = 0
      self.combat = 0
      self.strength = 0
      self.hearing = 0
      self.observation = 0
      self.reaction = 0
      
   def showStats(self):
      return '''
                  Stats:
Strength {}                    Observation {}
Combat   {}                    Reflexes    {}
Speed    {}                    Hearing     {}     
'''


