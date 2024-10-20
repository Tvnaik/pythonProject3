# 1) Write a Python program to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
#
# 2) Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

# 1)
#
# str=input("ENter the String")
#
# first=str[0]
# re=str[1:]
# next=first
#
# for i in re:
#     if i in first:
#         next+="$"
#     else:
#         next+=i
#
# print(next)


# 2)
# str=input("ENter the String")
# li=list(str)
# a=['g','n','i']
# if len(str)>=3:
#     if li[-1:-4:-1]==a[:]:
#         ab=str+"ly"
#         print(ab)
#     else:
#         aa=str+"ing"
#         print(aa)
# else:
#     print("Enter the string greater than 3")




