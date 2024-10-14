# Cho-han is a dice game played in gambling houses of feudal Japan. 
# Two six-sided dice are rolled in a cup, 
# and gamblers must guess if the sum is even (cho) or odd (han).

import random, sys

money = 5000


while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    while True:
        bet = input(f"You have {money} mon, the house takes 10% of your bet, every bet, how much are you willing to bet ?")
        if bet.isdecimal == False:
            print ("Enter a valid number.")
            continue
        elif int(bet) > money:
            print ("You do no have that much money.")
        else:
            money = (money-int(bet))
            print (f"Your money is now {money}")
            break

    while True: 
        chohan = input("Are you betting on CHO(even) or HAN(odd)").upper()
        if chohan != "CHO" and chohan != "HAN":
            print ("Enter either cho(even) or han(odd)")
            continue
        else:
            break

    print (f"Your bet is {bet} mon on {chohan}")
    bet = int(bet)/1.1
    bet = round(bet)
    print (f"The house takes 10%, your bet is now {bet} mon")
    print ("The dices are rolling !!")
    print (f" --{dice1}--{dice2}-- ")
    result = dice1 + dice2
    if result%2 == 0:
        print ("CHO(even) won !")
    else: 
        print ("HAN(odd) won !")

    if chohan == "CHO" and result%2 == 0:
        print ("Congratulations !")
        money = money + (bet*2)

    if chohan == "HAN" and result%2 != 0:
        print ("Congratulations !")
        money = money + (bet*2)

    if money == 0:
        print ("You don't have any money left !")
        sys.exit()




