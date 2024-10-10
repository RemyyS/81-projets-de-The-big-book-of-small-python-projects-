# In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. 
# The game offers one of the following hints in response to your guess: 
# “Pico” when your guess has a correct digit in the wrong place, 
# “Fermi” when your guess has a correct digit in the correct place, 
# and “Bagels” if your guess has no correct digits. 
# You have 10 tries to guess the secret number.

import pyinputplus as pyip
def main():
    sizeofinputnumber = 3 #The size of the number you want to play with
    numbertoguess = 0
    numberofguesses = 10 #Number of guesses allowed to the user
    guess = 0
    listfermipico = [] #List of "Fermi" and "Pico" that has to be randomized before being returned to not textualy give away the place of where the clue is obtained
    replayagain = ""
    sizeofinputnumber = pyip.inputNum("Enter the size of number you want to play with (default = 3)>")

    while len(str(numbertoguess)) > sizeofinputnumber or len(str(numbertoguess)) < sizeofinputnumber:
        numbertoguess = pyip.inputNum(f"Input {sizeofinputnumber} numbers to guess>")
        if len(str(numbertoguess)) > sizeofinputnumber or len(str(numbertoguess)) < sizeofinputnumber:
            print (f"Those are not {sizeofinputnumber} numbers. Try again.")


    print ("Try to guess the number.\n The program will give you a hint:\n "
        "\"Pico\" if you have a correct digit in the wrong place\n "
        "\"Fermi\" if you have a correct digit in the correct place\n "
        "\"Bagels\" if your guess has no correct digits")


    while len(str(guess)) > sizeofinputnumber or len(str(guess)) < sizeofinputnumber:
        guess = pyip.inputNum(f"Input {sizeofinputnumber} numbers as guess, you have {numberofguesses} guesses left >")
        if len(str(guess)) > sizeofinputnumber or len(str(guess)) < sizeofinputnumber:
            print (f"Those are not {sizeofinputnumber} numbers. Try again.")


    while numberofguesses > 0:
        listfermipico = []
        for i in range(len(str(guess))):
            if str(guess)[i] == str(numbertoguess)[i]:
                listfermipico.append('Fermi') #A good number is in the correct place
            elif str(guess)[i] in str(numbertoguess):
                listfermipico.append('Pico') #A good number is not at the right place
        if len(listfermipico) == 0:
            print ('Bagels flop!')
        if len(listfermipico) >= 1: 
            listfermipico.sort()
            print (listfermipico)
        
        numberofguesses -= 1
        guess = pyip.inputNum(f"Input {sizeofinputnumber} numbers as guess, you have {numberofguesses} guesses left >")
        if len(str(guess)) > sizeofinputnumber or len(str(guess)) < sizeofinputnumber:
            print (f"Those are not {sizeofinputnumber} numbers. Try again.")
        if guess == numbertoguess:
            break

    if guess == numbertoguess:
        replayagain = pyip.inputYesNo("Congratulations ! Would you like to play again ?")
        if replayagain == "yes":
            main()
                    


    if numberofguesses == 0:
        print (f"No more guesses left ! The answer was {numbertoguess}")

main()