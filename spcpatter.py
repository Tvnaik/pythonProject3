n=int(input("Enter the Number: "))

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    for k in range(0,n-i):
        print(" ",end=" ")
    for l in range(0,i+1):
        print("*",end="")
    print()
for i in range(1, n):
    for j in range(0, n-i):
        print("*", end="")
    for k in range(0,i+1):
        print(" ",end=" ")
    for l in range(0,n-i):
        print("*",end="")
    print()
