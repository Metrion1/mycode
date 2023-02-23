#!/usr/bin/python3
"""survive and escape"""
from random import randint

class Player:
    def __init__(self):
        self.health= 10
        self.attack_min= 5
        self.attack_max= 20
        self.prone= False
        
    def attack(self, other):
        roll= random.randint(1,20)
        
        if 1 < roll <= 6:
            print("Oops! You trip- you miss your turn to attack and take double damage this round!")
            self.prone= True
            
            # player falls, takes double damage the next turn, and they can't attack this round
        elif 7 <= roll <= 14:
            self.prone= False   # normal attack, regular damage
            if other.prone == True:
                 other.health -= randint(self.attack_min, self.attack_max) * 2
            else:
                 other.health -= randint(self.attack_min, self.attack_max)
               
        else:
            # double damage, critical hit!
            self.prone= False
            if other.prone == True:
                 other.health -= (self.attack_max * 2) * 2
            else:
                 other.health -= self.attack_max * 2

class Spider(Player):
    def __init__(self):
        self.health= 20
        self.attack_min= 5
        self.attack_max= 10
        self.prone= False
    
class Manticore:
    def __init__(self):
        self.health= 300
        self.attack_min= 100
        self.attack_max= 200
        self.prone= False
        
    def attack(self, other):
        other.health -= randint(self.attack_min, self.attack_max)
        
        
    
def left():
    print("You turn left and head down the hall and step into the murky room. As you stand there the shadows swirl together taking form! A Manticore stands in front of you three times the size of an elephant. Poison drips from its fangs and stinger... IT READIES TO ATTACK! YOU MUST STRIKE FIRST!! You READY A MIGHTY ATTACK!!!\n>")
    attack
    
def right():
    print("You make a right down a dimly lit hallway. As you step into the room, lights flood the room revealing a large chest. Gold and riches flood out of it as it slowly opens on its own! You take your fill and make your way out the other side to the exit...richer now that you were before!")

def forward():
    print("You proceed forward. After a short walk you find yourself in a room with high ceilings. As your eyes scale the walls, they are greeted by a pair in the dark then 3 more pairs...the eyes move togther and fixate on you. the start to glow a sinister green illuminating the head of the beast the symbol on its back starts to glow in unison revealing a spider the size of a carriage!! You pee your robe a little bit but steel yourself to the task ahead and ready an attack!\n>")

def badstart():
    """this is called when the player fails to make a good choice"""
    
def main():
    print("You awake in a dungeon. All your gear is intact but you are bleeding from the head. You don't know how you got here. Ahead of you lays a dungeon with three paths. you can barely see light at the end of each tunnel indicating an exit. but before each there seems to be a room shifting in and out of dimentions indicating strong magic or a trap. Either way you need to proceed.")

    user_input= input("Please choose a path: left, right, or forward\n>").lower()

    if user_input == "left":
        left()
        
    elif user_input == "right":
        right()
        
    elif user_input == "forward":
        forward()
    
    else:
        badstart()

if __name__ == "__main__":
    main()