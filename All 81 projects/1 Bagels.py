# In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. 
# The game offers one of the following hints in response to your guess: 
# “Pico” when your guess has a correct digit in the wrong place, 
# “Fermi” when your guess has a correct digit in the correct place, 
# and “Bagels” if your guess has no correct digits. 
# You have 10 tries to guess the secret number.

import pyinputplus as pyip

numberdemande = 0

while len(str(numberdemande)) > 3 or len(str(numberdemande)) < 3:
    numberdemande = pyip.inputNum("input 3 numbers>")
    if len(str(numberdemande)) > 3 or len(str(numberdemande)) < 3:
        print ("Those are not 3 numbers")





print (numberdemande)