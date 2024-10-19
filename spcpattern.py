n=int(input("Enter the Number: "))

for i in range(0,n,2):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("* ",end="")
    print()
for i in range(2,n,2):
    for j in range(0,i+2):
        print(" ",end="")
    for k in range(0,n-i-1):
        print("* ",end="")
    print()