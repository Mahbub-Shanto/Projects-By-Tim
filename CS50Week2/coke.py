amount_due=50
while amount_due>0:
    print("Amount Due:",amount_due)
    input_coin=int(input("Insert Coin:"))
    if input_coin in [25,10,5]:
        amount_due-=input_coin
change=abs(amount_due)
print("Change Owed:",change)
