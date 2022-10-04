  #Sign your name:Samuel Pattison
import random
'''
 1. Make the following program work.
   '''  
# print("This program takes three numbers and returns the sum.")
# total = 0
#
# for i in range(3):
#     x = int(input("Enter a number: "))
#     total += x
# print("The total is:", total)



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
# for i in range(2,101,2):
#     print(i)


'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
# x = 10
# while x > -1 :
#     print(x)
#     x -= 1
# print("Blast Off")
#



'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
# x = random.randrange(1,11)
# print(x)
#
#


'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total = 0
pos = 0
neg = 0
equ = 0
for i in range(7):
    x = int(input("Enter a number: "))
    total += x
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        equ += 1
print("The total is:", total)
print("You entered",pos,"positive numbers,",neg,"negative numbers, and",equ,"is the times you entered 0!")