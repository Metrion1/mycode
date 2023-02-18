#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game without a while True loop."""

round = 0
answer = " "

while round < 3 and answer != "Brian".title():
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of _____": ')
    if answer == "Brian":
        print("Correct!")
    elif round == 3:
        print("Sorry, the answer was Brian.")
    else:
        print("sorry. Try again!")
