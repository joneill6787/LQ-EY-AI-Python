'''
    Ask the user, "What is the capital of Australia?"

    If they answer "Canberra," print out "Canberra is the correct answer."
    If they answer "Sydney", print out "It's not Sydney, try again > "
    If they answer anything else print out, "___ is incorrect".

    Make sure the program allows someone who has answered "Sydney" to get a second go.

'''

capOfAussie = input("Hello, welcome to Australia, what is our capital?")

if capOfAussie == "Canberra":
    print("Canberra is the correct answer!")
elif capOfAussie == "Sydney":
    print("It's not Sydney, try again")
    print("Want to take another shot?")

    capOfAussie2 = input("Hello, welcome to Australia, what is our capital?")
    if capOfAussie2 == "Canberra":
        print("Canberra is the correct answer!")
    else:
        print("Could you please leave Australia, you're useless at geography")

else:
    print("Nope it aint: "+capOfAussie)