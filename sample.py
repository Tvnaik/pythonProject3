st=input("Enter the string: ")

first=st[0]
x=st[1:]
new=first

for i in x:
    if i in first:
        new+="$"
    else:
        new+=i
print(new)
