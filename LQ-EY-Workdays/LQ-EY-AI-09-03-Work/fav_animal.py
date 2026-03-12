'''
    Write a program that asks what the user's favourite animal is.
    
    If the user answers "dog" you should then ask the follow up question,
    "What is your favourite breed?"

    Print out, "Your favourite animal is a ___".

    However, if the person has answered a dog, you should print out . 
    "Your favourite breed of dog is a ___", instead.

    Don't try to build this program all in one go. Break it down into small 
    steps and build one step at a time.

'''

favAnimal=input("What is your favourite animal?")

if favAnimal == "dog":
    print("Your favourite animal is a",favAnimal)
    
    favBreed=input("What is your favourite breed of dog?")
    print("Nice I like",favBreed,"too!")
else:
    print("Your favourite animal is a",favAnimal)
    

