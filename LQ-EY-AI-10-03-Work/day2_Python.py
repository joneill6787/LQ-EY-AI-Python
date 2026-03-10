
    # [5] Indexing and Slicing Strings
myString="Hello Python"
'''
print("\nmyString length:",len(myString))

print("Getting the last character while knowing the length:",myString[len(myString)-1])
print("\n code below will break and give an index out of bounds error \n")
#print(myString[len(myString)])


# print(myString[-6::4])

print(myString[0:12:2])
print(myString[1:12:2])




pi = 3.14159265358979323846

print(f"{pi:.6f}")

r=1000000
print(f"{r:,}")



getCash=input("how much money do you have?\n")

cleanCash=round(float(getCash),2)

usaExchangeRate=1.2
euExchangeRate=1.1
hyruleExhchangeRate=2.34

convertCashUSA = round(cleanCash * usaExchangeRate,2)
convertCashEU = round(cleanCash * euExchangeRate,2)
converCashHyrule = round(cleanCash * hyruleExhchangeRate,2)


print(f"We can offer you:")
print(f"USA: {convertCashUSA:,}")
print(f"EU: {convertCashEU:,}")
print(f"Hyrule: {converCashHyrule:,} hiiiyaah!")



colours=["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet","Yellow"]

print(colours)
print(colours[0])

print(len(colours))

colours.append("Sponge")

print(colours)

colours.remove("Yellow")

print(colours)



print(list(range(3,14,2)))
print(list(range(3,14,4)))
print(list(range(3,14,8)))
print(list(range(0,-14,-1)))
print(list(range(0,-14,-2)))




for i in range(10):
    print(i)

'''

names = ['Rupert','Amy','Stan','Cartman','Kenny','Kyle']
namesSize = len(names)-1
numCheck=0


myMessage=""

for n in names:

    if numCheck < namesSize:
        myMessage = myMessage + n + ", "
    else:
        myMessage = myMessage + n

    numCheck+=1

    print(myMessage)