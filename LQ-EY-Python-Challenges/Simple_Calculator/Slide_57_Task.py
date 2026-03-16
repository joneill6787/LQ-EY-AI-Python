'''

Create a Simple Add that does the following:

    1, Asks the user for a number
    2, Asks the user for a mathematical operator
    3, Asks the user for a second number
    4, Prints out the number

'''



number1=int(input("Could we please have your first number?\n"))

operator=input("What mathematical option would you like to do?\n")

number2=int(input("Could we please have your second number?\n"))

if(operator=="*"):
    result=number1*number2
    print(f"You have chosen to multiply, therefore {number1} * {number2} = {result}")
elif(operator=="/"):
    result=number1/number2
    print(f"You have chosen to divide, therefore {number1} / {number2} = {result}")
elif(operator=="+"):
    result=number1+number2
    print(f"You have chosen addition, therefore {number1} + {number2} = {result}")
elif(operator=="-"):
    result=number1+number2
    print(f"You have chosen to subtraction, therefore {number1} - {number2} = {result}")
else:
    print(f"The operator you have entered: {operator} is not a recognised mathematical operator")