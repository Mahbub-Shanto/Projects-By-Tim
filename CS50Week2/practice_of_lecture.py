#Introduction of continue and break
while True:
    n=int(input("What's n: "))
    if n<=0:
        continue
    else:
        break
for _ in range(n):
    print("shapty")
    
    
#another way
while True:
    n=int(input("value of n: "))
    if n>0:
        break
for _ in range(n):
    print("shanto")
    