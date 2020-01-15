''' Developed by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Python-Mini-Projects '''

import random
import time
import sys
import os

#function to generate random number between 1 and 6
def generate():
    num = random.randint(1,6)
    return num

os.system('clear')

titl = "Welcome to Dice Rolling"
developed = "Developed by Shubham Agarwal"

print(" ",titl.center(100,' '))
print("\n", developed.center(100,' '))

while(True):
    roll = input("\nPress R to roll the dice: ")
    if roll == 'R' or roll == 'r':
        num = generate()

        ''' It will work in terminal only.
        If you are using Python shell, then comment the following 5 lines '''
        
        anim = "|/-\\"
        for i in range(10):
            time.sleep(0.1)
            sys.stdout.write("\r Rolling..." + anim[i % len(anim)])
            sys.stdout.flush()
            
        print("\nNumber is:\t", num)
    else:
        print("\nOops!! Wrong key pressed.")
        
    choice = input("\nDo you want to roll more? (Y/N): ")
    if choice == 'N' or choice == 'n':
        break

