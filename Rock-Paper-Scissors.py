# The apps first takes your choice.
p1 = input("Enter : ")
p2 = input("Enter : ")
a = "paper"
b = "rock"
c = "scissors"
# check that p1 is equal p2.
while p1 == p2:
    p1 = input("Enter again: ")
    p2 = input("Enter again: ")
# if p1 and p2 not equal start loop.
while p1 != p2:
    if p1 != p2:
        if p1 == a and p2 == b or p1 == b and p2 == c or p1 == c and p2 == a:
            print("p1 won!!")
        elif p2 == a and p1 == b or p2 == b and p1 == c or p2 == c and p1 == a:
            print("p2 won!!")
        # if user wants to continue input Enter otherwise
        # input quit
        print("If you want to continue press Enter otherwise enter 'quit' ")
        g = input("ENTER: ")
        if g == "":
            p1 = input("Enter again: ")
            p2 = input("Enter again: ")
        elif g == "quit":
            break
    # if user input p1 and p2 same thing takes again his/her choice
    # until he/she input p1 and p2 different.
    while p1 == p2:
        p1 = input("Enter, again: ")
        p2 = input("Enter, again: ")
print("End Game!!")
