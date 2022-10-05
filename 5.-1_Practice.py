# For 6loops are used a certain number of time
# while loops are used till a criteria is met
import random
# for i in range(5):
#     print(i)
# print("Done")
#
# for i in range(1,11): #first value inclusive second value exclusive
#     print(i)
# print("Done")
# for i in range(0,11,2):
#     print(i)
# print("Done")
# for i in range(10,-1,-2):
#     print(i)
# print("Done")
# for i in ["Hello","World"]:
#     print(i)
# for i in ("Hello World"):
#     print(i)
#
# total = 0
# for i in range(1,181):
#     total += i
# print(total)
#
# i=1
# while i<2**32:
#     print(i)
#     i*=2
#
# quit ="n"
# while quit.lower() == "n":
#     quit = input("Do you want to quit y/n")
# print("goodbye")
#
# done = False
# pers = 0
# while not done:
#     quit = input("Quit? y/n")
#     if quit.lower=="y":
#         done = True
#     else:
#         pers += 1
# print(pers)
# for i in range(10):
#     num = random.randrange(100,201,2)
#     print(num)
#
# for i in range(10):
#     num = random.randint(100,200)
#     print(num)
#
# for i in range(10):
#     num = random.random()*5+10
#     print(num)
done = False
while not done:
    num = random.randrange(1, 101)
    z = 0
    while not done:
        x = int(input("Guess the number? "))
        if x == num:
            print("You are correct!")
            print("You took",z,"guesses")
            i = input("Do you want to play again? y/n")
            if i.strip() == "n":
                done = True
            else:
                num = random.randrange(1, 101)
                z = 0
        elif x < num:
            print("The number is higher")
            z += 1
        else:
            print("The number is lower")
            z += 1