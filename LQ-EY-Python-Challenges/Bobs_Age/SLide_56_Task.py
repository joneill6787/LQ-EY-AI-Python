'''

Create a program that will use if, elif and else

Using if statements e.g. if bobsAge >.. etc

Task 1

    priknt out one of 3 messages depending on the age you have entered:

    + You are younger than Bob
    + You and Bob are the same age
    + You are older than Bob

'''


Bobsage = 21

yourageastext = int(input("What is your age?"))

if (Bobsage == yourageastext):
    print("You are the same age! Wohoo!")
elif(Bobsage > yourageastext):
    print("Bob is older than you, respect your elders?")
else:
    print("Bob is younger than you. Tragedy.")



