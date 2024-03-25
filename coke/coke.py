amount_due = 50

while amount_due > 0:
    coin = input("Insert Coin: ")
    if coin == "25" or coin == "10" or coin == "5":
        amount_due = amount_due - int(coin)
        if amount_due <= 0:
            print("Change Owed: " +  str(abs(amount_due)))
        else:
            print("Amount Due: " + str(amount_due))
    else:
        print("Amount Due: " + str(amount_due))
