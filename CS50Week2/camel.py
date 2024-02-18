camelCase=input("camelcase: ")
print("snake_case: ",end="")
for word in camelCase:
    if word.isupper():
        print("_"+word.lower(),end="")
    else:
        print(word,end="")

print()
