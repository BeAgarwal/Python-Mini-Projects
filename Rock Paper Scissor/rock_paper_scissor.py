''' Developed by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Python-Mini-Projects '''

import random
import os

os.system('clear')

p_point = 0
c_point = 0

def game(n,p,c):      # p for player and c for computer
    global p_point, c_point
    if p == c:
        print("Its a tie!")
        p_point += 10
        c_point += 10
    elif p == "rock" and c == "paper":
        c_point += 10
        print("Oops! You lose.")
    elif p == "paper" and c == "scissor":
        c_point += 10
        print("Oops! You lose.")
    elif p == "scissor" and c == "rock":
        c_point += 10
        print("Oops! You lose.")
    else:
        p_point += 10
        print("Hurray! You won.")
    board(n, p_point, c_point)


# function to print the points
def board(n, p, c):
    print("\n\n","RESULT".center(40,' '))
    print(n.center(20,' '),"COMPUTER".center(20,' '))
    print(str(p).center(20,' '),str(c).center(20,' '))

titl = "Welcome to Dice Rolling"
developed = "Developed by Shubham Agarwal"

print(" ",titl.center(100,' '))
print("\n", developed.center(100,' '))

list = ["rock","paper","scissor"]

name = input("Enter the player name: ")

while(True):
    enter = int(input("\n  Enter 1 for Rock,\n\t2 for Paper,\n\t3 for Scissor: "))
    while(enter < 1 and enter > 3):
        print("Oops! You have typed wrong key.")
        enter = int(input("\nEnter 1 for Rock,\n\t2 for Paper,\n\t3 for Scissor: "))

    p_choice = list[enter-1]        #player choice
    c_choice = random.choice(list)  #computer choice

    game(name, p_choice, c_choice)

    choice = input("Do you want to play more?(y/n) :")
    if choice =='n' or choice == 'N':
        print("\nGame Over")
        break
