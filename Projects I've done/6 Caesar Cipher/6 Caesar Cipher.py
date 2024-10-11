#The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. 
# It encrypts letters by shifting them over by a certain number of places in the alphabet. 
# We call the length of shift the key. 
# For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. 
# To decrypt the message, you must shift the encrypted letters in the opposite direction. 
# This program lets the user encrypt messages.


import pyinputplus as pyip



messagetoencrypt = ""
encryptedmessage = []
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

caesar_cipher = 3 #Key to the cipher, this encrypts the message by 3 letters further.



while True:
    messagetoencrypt = pyip.inputStr("Enter message to encrypt : ")
    break

messagetoencrypt = messagetoencrypt.upper()

for x in messagetoencrypt:
    if x in letters:
        position = str(letters).find(x)
        num = position + caesar_cipher
    
        if num > 26:
            num = num - 26 #Code for the loop around if the letter + the cipher is above the string length
        
        newcharacter = letters[num]
        encryptedmessage.append(newcharacter)

print (f"Your encrypted message is :",' '.join(encryptedmessage))

