#The Collatz sequence, 
# also called the 3n + 1 problem, 
# is the simplest impossible math problem. 
# From a starting number, n, follow three rules to get the next number in the sequence:
# If n is even, the next number n is n / 2.
# If n is odd, the next number n is n * 3 + 1.
# If n is 1, stop. Otherwise, repeat.

while True:
    startingnumber = input("Enter your starting number greater than 1:")
    if startingnumber.isdecimal() == False:
        print ("Enter a valid number.")
        continue
    elif int(startingnumber) <= 1:
        print ("Enter a number above 1")
        continue
    break

startingnumber = int(startingnumber)

while startingnumber != 1:
    if startingnumber %2 == 0:
        print (f"{startingnumber} is even, so we divide it by 2")
        startingnumber = startingnumber / 2
        print (f"The new number is now {startingnumber}")
        continue
    
    if startingnumber %2 != 0:
        print (f"{startingnumber} is odd, so we multiplie it by 3 and add 1")
        startingnumber = (startingnumber * 3) + 1
        print (f"The new number is {startingnumber}")
        continue

print (f"The collatz sequence is complete, the number is now {startingnumber}")