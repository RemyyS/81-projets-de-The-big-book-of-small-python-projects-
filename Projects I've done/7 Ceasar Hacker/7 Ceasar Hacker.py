#This program can hack messages encrypted with the Caesar cipher from Project 6, 
# even if you don’t know the key. 
# There are only 26 possible keys for the Caesar cipher, 
# so a computer can easily try all possible decryptions and display the results to the user. 
# In cryptography, we call this technique a brute-force attack.

import pyinputplus as pyip

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
messagetodecode = pyip.inputStr("Enter the message to brute-force decrypt (with no spaces):")
messagetodecode = messagetodecode.upper()


for y in range(26):
    decodedmessage = []
    for x in messagetodecode:
        if x in letters:
            position = str(letters).find(x)
            num = position - y
            
        if num < 0:
            num = num + 26
            
        newcharacter = letters[num]
        #print (newcharacter)
        decodedmessage.append(newcharacter)
        #print (decodedmessage)
    print(decodedmessage)
