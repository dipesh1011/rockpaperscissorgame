import sys
from random import randint
global finscore


def play():
    global finscore
    print("Lets begin")
    print("********************")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissor")
    num = int(input("Whats ur option:"))
    if num == 1:
        print("Your option is: Rock")
    elif num == 2:
        print("Your option is: Paper")
    elif num == 3:
        print("Your option is: Scissor")
    compsval = randint(1,3)
    print("##############")
    print("Computer option is:")
    if compsval == 1:
        print("Rock")
    elif compsval == 2:
        print("Paper")
    elif compsval == 3:
        print("Scissor")
    print("**************")
    while num == 1:
        if compsval == 1:
            print("Its draw")

        elif compsval == 2:
            print("Oops! You loose")
            finscore -= 1
            print("Your score is:",finscore)

        else:
            print("Congratulations!! You won")
            finscore += 1
            print("Your score is:",finscore)

        agn = input("Do you want to play again?(y|n)")
        if agn == "y":
            play()
        else:
            sys.exit()

    while num == 2:
        if compsval == 1:
            print("Congratulations!! You won")
            finscore += 1
            print("Your score is:",finscore)
        elif compsval == 2:
            print("Its draw")
        else:
            print("Oops! You loose")
            finscore -= 1
            print("Your score is:", finscore)
        agn = input("Do you want to play again?(y|n)")
        if agn == "y":
            play()
        else:
            sys.exit()

    while num == 3:
        if compsval == 1:
            print("Oops! You loose")
            finscore -= 1
            print("Your score is:",finscore)
        elif compsval == 2:
            print("Comgratulations!! You won")
            finscore += 1
            print("Your score is:",finscore)
        else:
            print("Its draw")
        agn = input("Do you want to play again?(y|n)")
        if agn == "y":
             play()
        else:
            sys.exit()
finscore = 0
play()

