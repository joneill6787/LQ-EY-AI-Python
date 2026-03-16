'''
Work with Range and loops

    1, Using range(), create a list that contains all even numbers to 30

    2, Using range(), create a loop that prints out the numbers 0, -3, -6 etc through to -30

    3, Using range(1,11), create a loop that prints out the square of 1 to 10.

    4, Using range(1,11), create a loop that prints out the squares of the even numbers
        and the cubes of the odd numbers from 1 to 10

'''

    # Task 1
        # The following loop will print 1 to 30

print("==Task 1==\n")
task1list30=range(1,31)

for i in task1list30:
    print(i)

    # Task 2
        # The following loop will print out the numbers 
        # 0, -3, -6 etc through to -30

print("\n==Task 2==\n")
task2list30=range(0,31,3)
    
for i in task2list30:
    print(-i)

    # Task 3
        # Using range(1,11), create a loop that prints out 
        # the square of 1 to 10.

print("\n==Task 3==\n")
task3list=range(1,11)

for i in task3list:
    print(i**2)

    # Task 4
        # Using range(1,11), create a loop that prints out 
        # the squares of the even numbers
        # and the cubes of the odd numbers from 1 to 10

    # Hint
        # To make this task easier, use modulus.
            # Modulus will return 1, if a number is odd, 0 if the number is even

print("\n==Task 4==\n")
task4list=range(1,11)


for i in task4list:
    if i%2==0:
        print(f"{i} squared:\t{i**2}")
    else:
        print(f"{i} cubed:\t{i**3}")

        # \t is a formating option for tab.