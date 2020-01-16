''' Developed by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Python-Mini-Projects '''

import random
import os

os.system('clear')

'''function to equalize the length of password and the entered length'''
def equal(l,s):
    while(len(s) != l):
        ch = chr(random.randint(48,122))
        s += ch
    return s

'''function to generate the random UpperCase, LowerCase, Digit, Special characters
    and merge with the string(password) '''
def generate(l,s):
    UC_letter = chr(random.randint(69,90))
    LC_letter = chr(random.randint(97,122))
    Digit = random.randint(0,9)
    Special_char = random.choice(['@','#','&','%','*','$','_'])

    s = UC_letter + Special_char + s + str(Digit) + LC_letter
    return equal(l,s)

titl = "Welcome to Password Generator"
developed = "Developed by Shubham Agarwal"

print(" ",titl.center(100,' '))
print("\n", developed.center(100,' '))

while(True):
    length = int(input("\nEnter the length of password: "))

    #minimum length of the password should be 6
    while length < 6:
        print("Password should be more than 6 characters.")
        length = int(input("\nEnter the length of password: "))

    choice = input("Do you want to add your string in password?(y/n): ")
    if choice == 'Y' or choice == 'y':
        string = input("Enter the string: ")
        if len(string) >= length:
            password = generate(length, string[0:(length-1)//2])
            print("Choose your password as: ", password)

        else:
            password = generate(length, string[0:length-4])
            print("Choose your password as: ", password)
            
    else:
        #If user does not want to add his/her own string
        string = ""
        password = generate(length,string)
        print("Choose your password as: ", password)

    choice = input("\nDo you want to generate the password once again? (y/n): ")
    if choice == 'N' or choice == 'n':
        break
    
print("\nThanks for using this feature. Hope you like it.!")
