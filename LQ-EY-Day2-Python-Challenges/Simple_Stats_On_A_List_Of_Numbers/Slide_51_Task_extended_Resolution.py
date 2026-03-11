import random

'''

The following code is an extension to the problem shown on Slide 52.

    We have a variable that stores a list of numbers starting at 20, 
    going up to 220 in increments of 5.

    In this extended challenge the list is randomised using the "random" library
    which you will see imported above, and the appropriate command below.

        Note: Each time you run the code, shuffle will reshuffle 
            the "numbers" list.

    Now do the following

Find the following:
    
    +   The minimum number from the list
    +   The maximum number from the list
    
        You will need to use if statements and a some loops to complete this challenge

'''

numbers = list(range(20,221,5))

    # The following command will shuffle the list of numbers for you.
random.shuffle(numbers)

    # Enter your code below this line

    # Problem 1
        # Find the lowest number in the list.

    # Solution:
    # To make things a little easier, we create a variable to hold the lowest
    # number in the list. This will make more sense in a moment

lowNumber = 0

    # We need to create a loop to go through the randomised list of numbers:

for i in numbers:

        # As 0 will always be lower than any value in the list
        # the first iteration of the loop needs to assign lowNumber to the first
        # value in the list of "numbers".
            # This will only happen on the first iteration
    
    if lowNumber == 0:
        print(f"Starting loop, setting lowNumber to: {i}")
        lowNumber = i

        # Then each time the loop iterates through we will compare if the current
        # number: i, is less than what lowNumber was set during the last iteration.
        # If i is less than what lowNumber is currently set to, the if statement
        # will set lowNumber = i, thus changing it to a lower value.

    if i < lowNumber:
        print(f"Yes, i: {i} is lower than lowNumber: {lowNumber}")
        print(f"Setting lowNumber to {i}")
        lowNumber = i

        # As the for loop continues, lowNumber will be reduced down to its lowest value.

    #Now print the lowest number.
print(f"The lowest Number in the list is: {lowNumber}")



    # Problem 2
        # Find the highest number in the list

    # Solution:
    # The solution to this problem is basically just the inverse of the lowNumber
    # All you need to do is repeat the same process:
        # Create a highNumber variable.
        # Loop through the list of "numbers" and replace highNumber with the higher value


highNumber = 0


for i in numbers:
    
    if highNumber == 0:
        print(f"Starting loop, setting highNumber to: {i}")
        highNumber = i

    if i > highNumber:
        print(f"Yes, i: {i} is higher than highNumber: {highNumber}")
        print(f"Setting highNumber to {i}")
        highNumber = i

print(f"The highest Number in the list is: {highNumber}")