toast = 154
guess = 560

guessstr = str(guess)
toaststr = str(toast)
toastlist = list(toaststr)

for i in range(len(str(toast))):
    if str(guess)[i] == str(toast)[i]:
        print ("Fermi")
    elif guessstr[i] in str(toast):
        print ("Pico")
    else: 
        print("padebol l'ékip")

