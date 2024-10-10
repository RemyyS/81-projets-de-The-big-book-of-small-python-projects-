#Rules:
# Try to get as close to 21 without going over.
# Kings, Queens, and Jacks are worth 10 points.
# Aces are worth 1 or 11 points.
# Cards 2 through 10 are worth their face value.
# (H)it to take another card
# (S)tand to stop taking cards.

import random
import sys


def returnplayerscore(playerhandscore):
    if ("J") in playerhandscore:
            playerhandscore.remove("J")
            playerhandscore.append(10)
    if ("Q") in playerhandscore:
            playerhandscore.remove("Q")
            playerhandscore.append(10)      
    if ("K") in playerhandscore:
            playerhandscore.remove("K") 
            playerhandscore.append(10)
    playerhandscore = sum(playerhandscore)
    return playerhandscore


def returndealerscore(dealerhandscore):
    if ("J") in dealerhandscore:
            dealerhandscore.remove("J")
            dealerhandscore.append(10)
    if ("Q") in dealerhandscore:
            dealerhandscore.remove("Q")
            dealerhandscore.append(10)      
    if ("K") in dealerhandscore:
            dealerhandscore.remove("K") 
            dealerhandscore.append(10)

    dealerhandscore = sum(dealerhandscore)
    return dealerhandscore
      
print ("Welcome to blacjack")

dealerhandscore = []
playerhandscore = []
deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]

random.shuffle(deck)
playerhandscore = [deck.pop(), deck.pop()]
dealerhandscore = [deck.pop(), deck.pop()]

print (f"You draw {playerhandscore}")
print (f"The dealer draws {dealerhandscore}")

returnplayerscore(playerhandscore)
returndealerscore(dealerhandscore)






