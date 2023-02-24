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
        roll= randint(1,20)
        print("die rolled:", roll)
        if 1 <= roll <= 6:
            print("Oops! You trip- you miss your turn to attack and take double damage this round!")
            self.prone= True
            
            # player falls, takes double damage the next turn, and they can't attack this round
        elif 7 <= roll <= 14:
            print("your attack strikes true! you cast Hellfire Arrow!")
            self.prone= False   # normal attack, regular damage
            if other.prone == True:
                 other.health -= randint(self.attack_min, self.attack_max) * 2
            else:
                 other.health -= randint(self.attack_min, self.attack_max)
               
        else:
            # double damage, critical hit!
            print("Power surges through you! a great spell bellows forth from your soul...AMATARASU!!")
            self.prone= False
            if other.prone == True:
                 other.health -= (self.attack_max * 2) * 2
            else:
                 other.health -= self.attack_max * 2
        
class Spider:
    def __init__(self):
        self.health= 20
        self.attack_min= 5
        self.attack_max= 5
        self.prone= False
    def attack(self, other):
        print("The Spider spews acid it tears through your clothing and sears off some flesh.")
        other.health -= randint(self.attack_min, self.attack_max)
    
class Manticore:
    def __init__(self):
        self.health= 300
        self.attack_min= 100
        self.attack_max= 200
        self.prone= False
        
    def attack(self, other):
        print("The Manticore spreads its glowing wings and curls his tail and points it at you. from the stinger spews a river of poison. It washes over you seeping into ever pore! you drown to death as you claw at you throat as blood seeps out of ever oraface.")
        other.health -= randint(self.attack_min, self.attack_max)
        
player= Player()
manticore= Manticore()
spider= Spider()    
    
def left():
    print("You turn left and head down the hall and step into the murky room. As you stand there the shadows swirl together taking form! A Manticore stands in front of you three times the size of an elephant. Poison drips from its fangs and stinger... IT READIES TO ATTACK! YOU MUST STRIKE FIRST!! You READY A MIGHTY ATTACK!!!\n>")
    user_input= input("Attack!! ATTACK OR DIE!!\n>").lower()

    while player.health > 0 and manticore.health > 0:
          player.attack(manticore)
          if manticore.health > 0:
            print("the Manticore shakes off the attack and prepares to retaliate... BRACE YOURSELF!!")
            manticore.attack(player)
          if player.health > 0:
            user_input= input("IT'S STILL ALIVE!!! strike again!\n>")
            if user_input != "attack":
                print("Your inaction has lead to the Manticore... ")
                player.health = 0
    if player.health > 0:
        print("you limp out of the cave gravely injured but alive to face another day!")
    elif player.health < 0:
        print("your bloated lifeless body now lies on the floor of the Manticore's den...forever in the dark.")
def right():
    print("You make a right down a dimly lit hallway. As you step into the room, lights flood the room revealing a large chest. Gold and riches flood out of it as it slowly opens on its own! You take your fill and make your way out the other side to the exit...richer now that you were before!")

def forward():
    print("You proceed forward. After a short walk you find yourself in a room with high ceilings. As your eyes scale the walls, they are greeted by a pair in the dark then 3 more pairs...the eyes move togther and fixate on you. the start to glow a sinister green illuminating the head of the beast the symbol on its back starts to glow in unison revealing a spider the size of a carriage!! You pee your robe a little bit but steel yourself to the task ahead and ready an attack!\n>")
    user_input= input("ATTACK to keep from ending up as spider food!!\n>").lower()
    while player.health > 0 and spider.health > 0:
          print(player.health, spider.health)
          player.attack(spider)
          if player.prone == True:
            print("the attack missed its mark!")
          if spider.health > 0:
            print("the Spider is hurt but not dead! the green it eminates begins to pulses as it begins its attack")
            user_input= input("IT'S STILL ALIVE!!! strike again!\n>")
            spider.attack(player)
          if player.health <= 0:
            print("the acid finally hits its mark dead center burning a hole through your chest killing you on the spot.")
          elif spider.health < 0:
            print("your spell incinerates the spider. you hear its screeching quickly grows silent as it stops squirming.")
            if user_input != "attack":
                print("Your inaction has lead to the Spider injecting you with digestive fluid. turning your insides to jelly. it draggs you off to feed its young.")
                player.health = 0
    if player.health > 0:
        print("you limp out of the cave injured but alive to face another day!")
    elif player.health < 0:
        print("The spider disapears int the dark. You spin around in fear of the direction it will attack from. Then a glowing web is spewed at you from a corner. as you trie to block it instantly melts through your clothes, then skin, organs and bones...leaving a pile of half melted parts on the floor in the dark.")

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
    
    else: user_input != {left, right, forward}
    badstart()

if __name__ == "__main__":
    main()