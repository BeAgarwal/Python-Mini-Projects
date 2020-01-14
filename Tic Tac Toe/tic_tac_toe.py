''' Developed by Shubham Agarwal

    Link: https://github.com/BeAgarwal/Python-Mini-Projects '''
    
import os
os.system('clear')              # change to 'clr' for windows
s = "WELCOME TO TIC TAC TOE"
developed = "Developed by Shubham Agarwal"
print(" ",s.center(120,' '))
print("\n", developed.center(120,' '))

print("\n Instruction to be followed:\n")
print("You have to type the number as mentioned in following figure.")
print("\t\t1\t2\t3\n\t\t4\t5\t6\n\t\t7\t8\t9\n")
print("****************************************************************************************************************")

print("\nEnter your name.")
name1=input("Player 1: ")
name2=input("Player 2: ")
print("\n**************************************************************************************************************")

welcome="Welcome {0} and {1}".format(name1.upper(),name2.upper())
print(" ", welcome.center(120,' '))

def printmodule(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j], end=' ')
        print()

def test(l,p):
    if(l[0][0]==l[0][1] and l[0][0]==l[0][2]):
        win=True #Horizontal1
        p+=1
    elif(l[1][0]==l[1][1] and l[1][0]==l[1][2]):
        win=True #Horizontal2
        p+=1
    elif(l[2][0]==l[2][1] and l[2][0]==l[2][2]):
        win=True #Horizontal3
        p+=1
    elif(l[0][0]==l[1][0] and l[0][0]==l[2][0]):
        win=True #Vertical1
        p+=1
    elif(l[0][1]==l[1][1] and l[0][1]==l[2][1]):
        win=True #Vertical2
        p+=1
    elif(l[0][2]==l[1][2] and l[0][2]==l[2][2]):
        win=True #Vertical3
        p+=1
    elif(l[0][0]==l[1][1] and l[0][0]==l[2][2]):
        win=True #DiagonalLeftToRight
        p+=1
    elif(l[0][2]==l[1][1] and l[0][2]==l[2][0]):
        win=True #DiagonalRightToLeft
        p+=1
    else:
        win=False
    return win,p

def result(p1,p2,name1,name2):
    if(p1>p2):
        print("\n\n HURRAY!!!",name1,"Won")
    elif(p2>p1):
        print("\n\n HURRAY!!!",name2,"Won")
    elif(p1==p2):
        print("\n\nIt's a tie,Man!!..")
        
    print("\n*********POINTS*********")
    print("---------------------------")
    print("||",name1,"||",name2,"||")
    print("||  ",p1," ||  ",p2," ||")
    print("---------------------------\n\n")
    
    a=input("Do you want to play more? (Y/N): ")
    if(a=='y' or a=='Y'):
        l=[['1','2','3'],['4','5','6'],['7','8','9']]
        i=1
        return l,i,True
    else:
        exit()
        
def verify(l):
    draw=True
    for i in  range(len(l)):
        for j in range(len(l[i])):
            if(l[i][j].isalpha()):
                continue
            else:
                draw=False
                break
    return draw

point1=0
point2=0
l=[['1','2','3'],['4','5','6'],['7','8','9']]
counter=True
i=1

while(counter):
    if i%2==0:
        s='X'
        n=name2
    else:
        s='O'
        n=name1
    i=i+1
    choice=int(input("Enter Your Choice %s: "%(n)))
    if(choice==1):
        l[0][0]=s
    elif(choice==2):
        l[0][1]=s
    elif(choice==3):
        l[0][2]=s
    elif(choice==4):
        l[1][0]=s
    elif(choice==5):
        l[1][1]=s
    elif(choice==6):
        l[1][2]=s
    elif(choice==7):
        l[2][0]=s
    elif(choice==8):
        l[2][1]=s
    elif(choice==9):
        l[2][2]=s
        
    printmodule(l)
    d=verify(l)
    
    if i%2==0:
        w,point1=test(l,point1)
    else:
        w,point2=test(l,point2)
    if(d):
        w=True
    if(w==True):
        l,i,counter=result(point1,point2,name1,name2)
