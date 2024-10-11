#The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. 
# It encrypts letters by shifting them over by a certain number of places in the alphabet. 
# We call the length of shift the key. 
# For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. 
# To decrypt the message, you must shift the encrypted letters in the opposite direction. 
# This program lets the user encrypt messages.


import pyinputplus as pyip

messagetoencrypt = ""
encryptedmessage = []
letters = "ABCDEFGIJKLMNOPQRSTUVWXYZ"

caesar_cipher = 3 #Key to the cipher, this encrypts the message by 3 letters further.

while True:
    messagetoencrypt = pyip.inputStr("Enter message to encrypt : ")
    if messagetoencrypt.isalpha() == False:
        print ("Do not enter numbers, Try again.")
        continue
    break

messagetoencrypt = messagetoencrypt.upper()

for letters in messagetoencrypt:
    append.letters[i+caesar_cipher]