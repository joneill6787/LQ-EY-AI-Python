'''
Write a short program that prints each number from 1 to 100 on a new line. 

For each multiple of 3, print "Fizz" instead of the number. 

For each multiple of 5, print "Buzz" instead of the number. 

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

    Hints:
        You will need to make use of the modulus function to complete this challenge.
        You will need to make use of a loop for this challenge.
        You will need to make use of if statements
    
    One Final tip:
        If you do use if statements the order they are called in is important!


Good Luck!


'''

    # We need to establish a variable to count up from 0 to 100

i = 0

    # With the variable established we can now set up our loop.
        # In my example I have used a WHILE loop simply because I know that the loop
        # Must stop at 100.
            # If you would prefer to use a FOR loop, you can do so as well!

while i <=100:

        # In the following if statements I will use modulus to find what we are looking for
        # Modulus (%) returns 0 if a number can be divided by another without leaving a remainder
            # Further down the code you will see a more comprehensive explanation of why the
            # if/elif check is set up this way and why the order is important.                  

    if i%3 == 0 and i%5 == 0:
        print(i,"FizzBuzz")
    elif i%3 == 0:
        print(i,"Fizz")
    elif i%5 == 0:
        print(i,"Buzz")
    else:
        print(i)
    
        # We now need to increment the value of i by 1 once all if/elif statements have
        # been evaluated.
            # This is done with a simple i+=1
            # The following article shows you how you do these increments/decrements
            # https://codegym.cc/groups/posts/increment-and-decrement-in-python

    i+=1



    # Why the order of the if/elif matters:
        # When you use % you can easily work if i can be divided by 3 or 5
        # because a 0 will be the result. This can then be worked into you if loops
        # If i%3=0, it means the number can be divided by 3, thus we print Fizz.
        # If i%5=0, it means the number can be divided by 5, thus we print Buzz.
            # Now printing FizzBuzz may seem tricky at first, but if you use an if/elif combo
            # the first condition that is met in the if/elif combo will print a result.
        # So what you will want to do is check the least likely thing to occur first
        # I.E.: a number divisable by both 3 and 5, then move on to check the  
        # individual numbers.

            # To work through this logic we know the following:
            # If i = 3 or 6 or 9 or 12, it will not meet the first if statement as 
            # none of these numbers are divisable by 5. 
                # Therefore: if i%3 == 0 and i%5 == 0 will always be skipped.
            # Likewise, if i = 5 or 10, these numbers are not divisible by 3, so
            # if i%3 == 0 and i%5 == 0 will not evaluate.

            # Therefore the first time a number that is both divisible by 3 and 5,
            # 15, will trigger the first if condition and step out of the if/elif
            # check and print FizzBuzz.
            # Even though 15 would technically meet the condition for if i%3 == 0
            # in the elif check and i%5 == 0 in elif check after, because the first
            # condition of the if statement is met: "if i%3 == 0 and i%5 == 0:" the
            # code does not evaluate any further.

        # If you want to take this a step further and see why it is important
        # to use an if/elif instead of three if statements, feel free to change
        # the code to use three ifs instead, or run the below code (after removing
        # the comments) to see what happens


'''

alternative_i=0

while alternative_i <=100:


    if alternative_i%3 == 0 and alternative_i%5 == 0:
        print(alternative_i,"FizzBuzz")
    else:
        print(alternative_i)
    
    if alternative_i%3 == 0:
        print(alternative_i,"Fizz")
    else:
        print(alternative_i)

    if alternative_i%5 == 0:
        print(alternative_i,"Buzz")
    else:
        print(alternative_i)

    alternative_i+=1

    '''