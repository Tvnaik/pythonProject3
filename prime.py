# lis=[num for num in range(2,101) if all(num%i!=0 for i in range(2,int(num**0.5)+1))]
# print(lis)

# li=[i for i in range(10)]
# print(li[-3:-11:-1])

str=input("Enter the string")
dic={}
for i in str:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)

