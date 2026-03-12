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

'''

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