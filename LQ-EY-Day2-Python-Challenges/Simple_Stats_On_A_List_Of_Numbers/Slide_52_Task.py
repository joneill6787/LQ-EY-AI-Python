'''

The following code generates a list of numbers starting at 20, 
    going up to 220 in increments of 5:

Find the following:
    
    +   The minimum number from the list
    +   The maximum number from the list
    +   The sum of all the numbers in the list

'''


numbers = list(range(20,221,5))

# print(numbers)

    # Problem 1
        # Find lowest Number from list

print(f"Lowest Number is {numbers[0]}")


    # Problem 2
        # Find Highest Number from list

print(f"Highest Number: {numbers[-1]}")

    # Problem 3
        # Find Total of all values in list

totalCount = 0

for i in numbers:
    totalCount = totalCount + i

print(f"Total Count: {totalCount}")