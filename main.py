# import necessary libraries

import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np
from tempest import *
from darkknight import *
from totemist import *

# define important variables

# Character stats
armor = 0
evasion = 0
shield = 0
vitality = 0
finesse = 0
acuity = 0
health = 0
damage = 0
damage_multiplier = 0
slot_1 = ""
class_pick = ""

# Game Start / Name decision

print("Welcome to Verimestia RPG, created by Aidan Marsters!\n")
time.sleep(2.5)
print("Verimestia is a mystical land filled with turbulent twists & many regions to explore!\n")
time.sleep(2.5)
print("To start, what would you like to name your character?")
time.sleep(1.5)
name = input("Enter your character name:\n")
time.sleep(2)
print("\nWelcome to Verimestia",name,". Now you can pick your class!")
time.sleep(2)

# Class pick
tempest_desc()
arb1 = input("Press 1 if you want to see the other classes or 2 if you want to pick tempest\nChoice: ")
arb1 = int(arb1)
if arb1 == 1:
    darkknight_desc()
    arb2 = input("Press 1 if you want to see the final class or 2 if you want to pick Dark Knight\nChoice: ")
    arb2 = int(arb2)
    if arb2 == 2:
        class_pick = "Dark Knight"
        slot_1 = "Apprentice Scimitar"
    if arb2 == 1:
        totemist_desc()
        print("Now that you've seen each class it is time to pick!\n")
        time.sleep(2)
        arb3 = input("Choose 1 for the Tempest, 2 for the Dark Knight, and 3 for the Totemist\nChoice: ")
        arb3 = int(arb3)
        if arb3 == 1:
            class_pick = "Tempest"
            slot_1 = "Apprentice Wand"
        elif arb3 == 2:
            class_pick = "Dark Knight"
            slot_1 = "Apprentice Scimitar"
        elif arb3 == 3:
            class_pick = "Totemist"
            slot_1 = "Apprentice Battle Axe"
elif arb1 == 2:
    class_pick = "Tempest"
    slot_1 = "Apprentice Wand"
else:
    print("That is not a valid value")

print(name,"You have chosen:",class_pick,"\n")
time.sleep(2)
print("You are now a powerful",class_pick,"yielding a",slot_1,"\nenjoy all that Verimestia has to offer!")
time.sleep(8)
print("\n"*100)
print("You've awoken in a daze, confused by how you got here or why you are here.\n As your senses slowly come back a man runs in your direction...")
time.sleep(4)
print(name,"..",name,"Get up we need to leave now!")
time.sleep(2)









