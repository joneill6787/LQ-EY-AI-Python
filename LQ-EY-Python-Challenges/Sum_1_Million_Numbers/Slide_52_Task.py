'''
Creat a list that contains the numbers 1 1o 1 million

    + Use min to verify that the first number in the list is 1
    + Use max to verify that the last number in the list is 1 million

Sum the numbers 1 to 1 million and display the result as a sentence.
    For Example:
        "The sum of the numbers 1 to 1 million is: 'x'"
    

'''

millionNumbers = list(range(1,1000001))

print(millionNumbers[0])
print(millionNumbers[-1])

totalValue = 0

for i in millionNumbers:
    totalValue += i

print(f"The sum of the numbers 1 to 1 million is: {totalValue}")