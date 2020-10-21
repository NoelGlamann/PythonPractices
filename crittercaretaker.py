#!usr/bin/python3
#Noel Glamann
#06 November 2019

"""      Critter Class for Virtual Pet

The critter has three attributes: fitness, happiness, and 
satiation(being well-fed). The values range from 0 - 120. 
Death occurs when any attribute reaches 0. Playing, feeding, 
and excersizing are all functions that raise the corresponding 
attributes by a random value. The purpose of the game is to 
keep the critter alive as long as posisble. 
"""

from datetime import datetime
import random as r
from faces import *

playing_with = False

class Critter(object):
    
    def __init__(self, name):
        self.happiness = 120
        self.fittness = 120
        self.satiation = 120
        self.birthday = datetime.now()
        self.name = name
    
    def talk(self):
        msg = "Hi, I'm a critter named "+ self.name + "! \n"
        msg += "I was born "+str(self.birthday.date()) +"\n"
        msg += "My happiness score: " + str(self.happiness) + "\n"
        msg += "My fittness score: " + str(self.fittness) + "\n"
        msg += "My 'full tummy' score: " + str(self.satiation) + "\n"
    
        print(msg)
        print()
        
    def play(self):
        print("Bet you can't get me!")
        print("hehehehe")
        print()
        self.happiness += r.randint(1,15)   
        if self.happiness > 120:
            self.happiness = 120
    
    def excersize(self):
        print("Let's get these gains!")
        print("One.... Two.... Done?")
        print()
        self.fittness += r.randint(1,15)   
        if self.fittness > 120:
            self.fittness = 120
        
    def feed(self):
        print("I think I have a case of the munchies...")
        print("*munch, crunch, munch*")
        print()
        self.satiation += r.randint(1,15)   
        if self.satiation > 120:
            self.satiation= 120
    
    def slow_death(self):
        ''' reduce each attribute by random amount 1-5 '''
        self.happiness -= r.randint(1,5)
        self.fittness -= r.randint(1,5)
        self.satiation -= r.randint(1,5)
        
    
if __name__ == "__main__":
    test_critter = Critter("Gladis")
    
    test_critter.talk()
    
    test_critter.slow_death()
    test_critter.slow_death()
    test_critter.slow_death()
    
    test_critter.talk()

    test_critter.feed()
    test_critter.excersize()
    test_critter.talk()
    draw_happy()
    