'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''
import random
print("Welcome to the thunder dome!")
print("Each time you play you will have a choice, 1 for rock, 2 for paper, 3 for scissors, and 4 for quit.")
win = 0
lose = 0
tie = 0
done = False
while not done:
    comp = random.randrange(1,4)
    pc = int(input("What is your choice? "))
    if pc == 3:
        print("You chose scissors")
        if comp == 1:
            print("The computer chose rock")
            print("You lose")
            lose += 1
        elif comp == 2:
            print("The computer chose paper")
            print("You win")
            win += 1
        else:
            print("The computer chose scissors")
            print("You tie")
            tie += 1
    elif pc == 2:
        print("You chose paper")
        if comp == 1:
            print("The computer chose rock")
            print("You win")
            win += 1
        elif comp == 2:
            print("The computer chose paper")
            print("You tie")
            tie += 1
        else:
            print("The computer chose scissors")
            print("You lose")
            lose +=1
    elif pc == 1:
        print("You chose rock")
        if comp == 1:
            print("The computer chose rock")
            print("You tie")
            tie += 1
        elif comp == 2:
            print("The computer chose paper")
            print("You lose")
            lose += 1
        else:
            print("The computer chose scissors")
            print("You win")
            win += 1
    else:
        done = True
print("You won",win,"game. You lost",lose,"games. You tied",tie,"times.")
print("Peace out")