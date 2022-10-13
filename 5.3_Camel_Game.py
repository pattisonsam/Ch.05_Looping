'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
done = False
rat = 5
loc = 0
stu = -20
thirst = 0
age = 0
print("Welcome to the teacher game!")
print("Your name is Mr. Hermon and you are running from kids who you've wronged.")
print("While running you still will need to do your job and survive. :( ")
print("Each turn you will have a few options:")
print("Run full speed!")
print("Run moderate speed")
print("Code for your job")
print("Eat and drink")
print("Rest")
print("Check the code")
print("Quit")
print("All of these options do something different, I could explain it, but its more fun if you figure it out yourself.")
print("Have fun!")
while not done:
    print("-----------------------------------------------------")
    #Testing the conditions to see if something is wrong with you
    if loc >= 200:
        print("The students have finally given up the chase. You win!")
        break
    if thirst == 6:
        print("You have gotten too hungry. You lose.")
        break
    elif thirst >= 4 and loc > stu:
        print("You're getting hungry you should eat")
    if age == 10:
        z = random.randrange(1, 21)
        print("Because of you age you need to rest")
        stu += z
        print("-----------------------------------------------------")
    elif age >= 5 and loc > stu:
        print("You should rest your age is catching up to you.")
    if loc <= stu:
        print("The students have overtaken you. You lose.")
        break
    elif loc-stu < 15:
        print("The students are getting close. RUN!")
    o = random.randrange(0, 20)
    if o == 13:
        print("***************************************************")
        print("You found a school willing to help you on your journey")
        print("***************************************************")
        thirst = 0
        rat = 5
        age = 0
    #Your choices
    print("A. Run full speed!")
    print("B. Run moderate speed")
    print("C. Code for your job")
    print("D. Eat and drink")
    print("E. Rest")
    print("F. Check the code")
    print("Q. Quit")
    x = input("What is you choice: ")
    #Choice A
    if x.upper().strip() == "A":
        print("You move forward at full speed")
        y = random.randrange(5,9)
        print("You moved forward", y, "miles")
        z = random.randrange(4,8)
        loc += y
        thirst += 1
        stu += z
        age += 2
    # Choice B
    elif x.upper().strip() == "B":
        print("You move forward at moderate speed")
        y = random.randrange(1,6)
        print("You moved forward", y, "miles")
        z = random.randrange(3,8)
        loc += y
        thirst += 1
        stu += z
        age += 1
    # Choice C
    elif x.upper().strip() == "C":
        y = random.randrange(1,101)
        z = random.randrange(3, 8)
        if y == 69:
            print("The kids run from you brilliance.")
            print("You win")
            break
        else:
            print("You work so hard but get nothing in return")
            thirst += 1
            stu += z
    # Choice D
    elif x.upper().strip() == "D":
        z = random.randrange(3, 8)
        if rat == 0:
            print("You have no rations")
            stu += z
            thirst += 1
        else:
            print("You feast because you hunger it")
            rat -= 1
            thirst = 0
            stu += z
    # Choice E
    elif x.upper().strip() == "E":
        z = random.randrange(3, 8)
        print("Your getting old and need to rest.")
        age = 0
        thirst += 1
        stu += z
    # Choice F
    elif x.upper().strip() == "F":
        print("Your location is",loc)
        print("The kids are at",stu)
        print("Your rations are",rat)
        print("Your hunger and thirst is",thirst)
    # Choice Q
    elif x.upper().strip() == "Q":
        break
    # Not a choice
    else:
        print("Not an option choose again.")
print("Thanks for playing")
