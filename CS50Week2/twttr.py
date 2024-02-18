input=str(input("Input: ")).strip()
print("Output:",end="")
v=["a","e","i","o","u"]
for word in input:
    if word.lower() not in v:
        print(word,end="")
print()

