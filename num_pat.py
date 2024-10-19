n=int(input("Enter the Number: "))

for i in range(0,n):
    for j in range(1,n-i):
        print(" ",end="")
    for k in range(1,i+2):
        print(k,end=" ")
    print()
for i in range(0,n):
    for j in range(1,i+2):
        print(" ",end="")
    for k in range(1,n-i):
        print(k,end=" ")
    print()