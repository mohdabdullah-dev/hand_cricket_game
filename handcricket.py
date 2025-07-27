import random


def Batting():
    y_score=0
    c_score=0
    while True:
        bat=int(input("Bat : "))
        bowl=random.randint(1,6)
        print("Computer chooses : ",bowl)
        if bat==bowl:
            print("You are Out")
            print(f"your final score {y_score}")
            break
        else:
            y_score+=bat
            print(f"your score {y_score}")
    print("It's Your turn for bowling")
    while True:
        bat=random.randint(1,6)
        bowl=int(input("Bowl : "))
        print("Computer chooses : ",bat)
        if bat==bowl:
            print("You took a wicket! WELL DONE")
            print(f"computer final score {c_score}")
            break
        else:
            c_score+=bat
            if y_score<c_score:
                break
            print(f"computer score {c_score}")
    if c_score>y_score:
        print("Computer won")
    elif y_score>c_score:
        print("CONGRATULATIONS YOU WON")
    else:
        print("tie")
    print("Your score : ",y_score)
    print("Computer score : ",c_score)



def Bowling():
    y_score=0
    c_score=0
    while True:
        bat=random.randint(1,6)
        bowl=int(input("Bowl : "))
        print("Computer chooses : ",bat)
        if bat==bowl:
            print("You took a wicket! WELL DONE")
            print(f"computer final score {c_score}")
            break
        else:
            c_score+=bat
            print(f"computer score {c_score}")
    print("It's Your turn for batting")
    while True:
        bat=int(input("Bat : "))
        bowl=random.randint(1,6)
        print("Computer chooses : ",bowl)
        if bat==bowl:
            print("You are Out")
            print(f"your final score {y_score}")
            break
        else:
            y_score+=bat
            if y_score>c_score:
                break
            print(f"your score {y_score}")
    if c_score>y_score:
        print("Computer won")
    elif y_score>c_score:
        print("CONGRATULATIONS YOU WON")
    else:
        print("tie")
    print("Your score : ",y_score)
    print("Computer score : ",c_score)




print("1 for Head", "2 for Tails",sep="\n")
t=int(input(""))
ch=int(input("choose b/w 1 and 5 : "))
toss=random.randint(1,5)
print(f"computer : {toss}")
if ((ch+toss)%2==0 and t==2) or ((ch+toss)%2!=0 and t==1):
    print("YOU won Toss")
    choice=int(input("1 for batting\n2 for bowling : "))
    if choice==1:
        print("YOU choose batting")
        Batting()
    else:
        print("YOU choose Bowling")
        Bowling()
else:
    print("Computer won toss : ")
    choice=random.randint(1,2)
    if choice==1:
        print("Computer choose batting")
        Bowling()
    else:
        print("Computer choose Bowling")
        Batting()