messagetoencrypt = ["T", "E", "S", "T"]
encryptedmessage = []
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caesar_cipher = 3





for x in messagetoencrypt:
    if x in letters:
        position = str(letters).find(x)
        print (position)
        newpos = position + caesar_cipher
        print (newpos)
        newcharacter = letters[newpos]
        print (newcharacter)
        encryptedmessage.append(newcharacter)
        print(encryptedmessage)
     



print(encryptedmessage)

#print (num)
#for x in messagetoencrypt:
    #encryptedmessage.append(str(letters).find(x))


encryptedmessage.append(letters[2])
print (encryptedmessage)