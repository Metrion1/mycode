
dragon= 0
liger= 0
griffin= 0
pheonix= 0
stick= 0
while True:
    q1= input("""Choose a birth.
    a. in a foreign land to nobles 
    b. In a cave, left by dying mother
    c. in the swamps to a pack of cannibals
    d. in a void dimension adrif for eons
    e. in a hidden city of powerful magic users
    >""")

    if q1 == "a":
        stick += 1
        break
    elif q1 == "b":
        pheonix += 1
        break
    elif q1 == "c":
        liger += 1
        break
    elif q1 == "d":
        dragon += 1
        break
    elif q1 == "e":
        griffin =+ 1
        break

while True:
    q2= input("""Choose and upbringing.
    a. Raised in the wild forced to hunt for every meal
    b. allowed to attend school, but drops out to persue a life of crime
    c. was forced into a fighting arena at young age
    d. kills caretakers for not giving you everyhting you wanted
    e. tried to walk a straight path but was falsely accused and thrown in jail
    >""")

    if q2== "a":
        liger =+ 1
        break
    elif q2== "b":
        griffin =+ 1
        break
    elif q2== "c":
     dragon =+ 1
     break
    elif q2== "d":
        stick =+ 1
        break
    elif q2== "e":
        pheonix =+ 1
        break

while True:
    q3= input(""" choose a life.
    a. Join the military and fight for your country
    b. live a life of luxury, travel and excess.
    c. learn powerfull magic from sages and enslave a world
    d. dedicate yourself to the arts
    e. abandon scociety and live secluded in the mountains.
    >""")
    
    if q3== "a":
        liger =+ 1
        break
    elif q3== "b":
        stick =+ 1
        break
    elif q3== "c":
        dragon =+ 1
        break
    elif q3== "d":
        pheonix =+ 1
        break
    elif q3== "e":
        griffin =+ 1
        break

while True:
    q3= input(""" The enemy are at your gates! what do you do?.
    a. Charge forward claim as many lives as possible before you are cut down
    b. escape through the secret passages with as much as you can carry
    c. rain hellfire down on their heads from your tower
    d. sheild yourself with the servants and lessers as you make your escape
    e. negotiate
    >""")
    
    if q3== "a":
        liger =+ 1
        break
    elif q3== "b":
        pheonix =+ 1
        break
    elif q3== "c":
        dragon =+ 1
        break
    elif q3== "d":
        stick =+ 1
        break
    elif q3== "e":
        griffin =+ 1
        break

while True:
    q3= input(""" choose how you die.
    a. flesh eating bacteria
    b. you dont you are endless.
    c. alone in a dark cold cave
    d. surrounded by friends and family having lived a long life.
    e. during sex... your heart gives out.
    >""")
    
    if q3== "a":
        liger =+ 1
        break
    elif q3== "b":
        dragon =+ 1
        break
    elif q3== "c":
        stick =+ 1
        break
    elif q3== "d":
        pheonix =+ 1
        break
    elif q3== "e":
        griffin =+ 1
        break

print(f"""
FINAL SCORES:
Dragon: {dragon}
Liger: {liger}
Griffin: {griffin}
Pheonix: {pheonix}
Stick: {stick}""")