#This program uses a multiline string as a bitmap, 
# a 2D image with only two possible colors for each pixel, 
# to determine how it should display a message from the user. 
# In this bitmap, space characters represent an empty space, and all other characters are replaced by characters in the user’s message. 
# The provided bitmap resembles a world map, but you can change this to any image you’d like. 
# The binary simplicity of the space-or-message-characters system makes it good for beginners. 
# Try experimenting with different messages to see what the results look like!

import sys

# (!) Try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of this string:
# (You can also copy and paste this string from
# https://inventwithpython.com/bitmapworld.txt)
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
         *************          **  * **** ** ************** *
          *********            *******   **************** * *
           ********           ***************************  *
  *        * **** ***         *************** ******  ** *
              ****  *         ***************   *** ***  *
                ******         *************    **   **  *
                ********        *************    *  ** ***
                 ********         ********          * *** ****
                  *********         ******  *        **** ** * **
                  *********         ****** * *           *** *   *
                    ******          ***** **             *****   *
                    *****            **** *            ********
                   *****             ****              *********
                   ****     *         **                 *******   *
                   ***     ***                                  *    *
                   **     *****                    *
...................................................................."""
print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
   # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print()  # Print a newline.