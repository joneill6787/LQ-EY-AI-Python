'''

Create a simple app that asks for: 

    + The total bill
    + The number of people
    + The percentage you want to tip.

'''


billAmount = float(input("What was your total bill for tonights dinner?\n"))
print(f"Your total bill came to the amount of: {billAmount}")

partySize = int(input("How big is your party?\n"))

if(partySize >= 1):
    print(f"There are {partySize} people in your party")
else:
    print("Awkward...")

tipAmount = int(input("What % do you want to tip? Please enter a whole number?\n"))
print(f"You will tip {tipAmount}%")

tipAmountCalc = (tipAmount/100)+1

totalBill = round(billAmount*tipAmountCalc,2)

totalSplit = round(totalBill/partySize,2)


print(tipAmountCalc)
print(f"Total bill with tip comes to: {totalBill}, each member will have to pay {totalSplit}")