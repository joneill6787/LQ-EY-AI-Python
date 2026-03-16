'''

Using the provided list print out the following:

    + Max
    + Min
    + Sum
    + Length
    + Average

'''

numberList = [12,5,19,15,19,7,15,2,17,14,15,18,13,0,12,8,10,18,18]
listSize=len(numberList)
sumList = 0

for i in numberList:
    sumList+=i


print(f"The minimum number on your list is: {min(numberList)}")
print(f"The maximum number on your list is: {max(numberList)}")
print(f"The sum of the list of numbers: {sumList}")
print(f"The list contains {listSize} elements")
print(f"The average value in the list rounded to nearest int = {int(round(sumList/listSize))}")