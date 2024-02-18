#demonstration of list and dict
students=["Harmione","Shupty","Harry"]
print(students[1])

#or

for student in students:
    print(student)
#as values in students are strings we can't  use range so we used len function first to get their range then range function
#also we used i+1 to get the value starting from 1 not from 0

for i in range(len(students)):
    print(i+1,students[i])
    
#dictionaries using dict data type
stud = {
    "harry":"gazipur",
    "shupty":"mymensings",
    "shanto":"gazipur"
    
}


print(stud["shupty"])


#using for loop
for student in stud:
    print(student,stud[student],sep=",")
    
#Demonstrates iterating over a list of dict objects
st=[
    {"name":"shupty","home":"mymensingh"},
    {"name":"shanto","home":"mymensingh"},
]
for s in st:
    print(s["name"],s["home"], sep ="and")