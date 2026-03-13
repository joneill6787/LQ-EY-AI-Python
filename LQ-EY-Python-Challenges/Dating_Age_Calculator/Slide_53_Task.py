'''
Bit of a wild one this one:

Part 1:

    Write a program that calculates the youngest person you can date.

    The premise that the youngest person you can date is half your age plus 7 years.
        So, if you are 26, the youngest person you can date is 20.
        If you are 50, the youngest person you can date is 32.

        Add a rule so that the youngest age you can date is 18, no matter what

Part 2:

    Modify the program so that it also works out the oldest person you can date.


Part 3:

    For every 1 million you have in the bank, you can date someone a year younger.
        Modify your algorithm so that it takes into account your
        net worth in millions.
'''


def testAgeCalculator():
    age=[18,25,30,45,60,80,100]

    for i in age:

        dateAgeYoung = round((i/2)+7)
        dateAgeOld = round((i*2)-7)

        if dateAgeYoung < 18:
            print(f"You are {i} the youngest person you can date is the following age 18")
            print(f"You are {i} the oldest person you can date is the following age {dateAgeOld}")
        else:
            print(f"You are {i} the youngest person you can date is the following age {dateAgeYoung}")
            print(f"You are {i} the oldest person you can date is the following age {dateAgeOld}")

        print()


def datingAgeCalculator():

        # This function will resolve tasks 1 and 2

    userAge= int(input("Please could I have your age so we can calculate who you can date?\n"))

    dateAgeYoung = round((userAge/2)+7)
    dateAgeOld = round((userAge*2)-7)

    if userAge < 18:
        print(f"You are {userAge} the youngest person you can date is the following age 18")
        print(f"You are {userAge} the oldest person you can date is the following age {dateAgeOld}")
    else:
        print(f"You are {userAge} the youngest person you can date is the following age {dateAgeYoung}")
        print(f"You are {userAge} the oldest person you can date is the following age {dateAgeOld}")


def datingAgeMoneyCalculator():

        # This function will resolve tasks 

    userAge= int(input("Please could I have your age so we can calculate who you can date?\n"))
    userWealth= int(input("And how much do you earn in millions per year?\n"))

    if(userWealth>100):
        print("Well aint you rich? Can you spare me a few million?")

    dateAgeYoung = round((userAge/2)+7-userWealth)
    dateAgeOld = round((userAge*2)-7-userWealth)

    if dateAgeYoung < 18:
        print(f"You are {userAge} and have {userWealth} million in the bank")
        print(f"The youngest person you can date is the following age: 18")
        if dateAgeOld < 18:
            print(f"The oldest person you can date is the following age: 18")
        else:
            print(f"The oldest person you can date is the following age: {dateAgeOld}")
    else:
        print(f"You are {userAge} the youngest person you can date is the following age {dateAgeYoung}")
        print(f"You are {userAge} the oldest person you can date is the following age {dateAgeOld}")


datingAgeMoneyCalculator()