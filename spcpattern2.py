n=int(input("Enter the number: "))

for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(1,i+2):
        print(k,end="")
    for l in range(i,0,-1):
        print(l,end="")
    print()