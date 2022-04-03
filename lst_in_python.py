# lst = list()
# s = 0
# for i in range(1,11):
#     input_user = int(input("Enter a No: "))
#     lst.append(input_user)
#     s = s + input_user
# print("list in user : ",lst)
# print("sum of all no : ",s)

# second type to solve this programmne
# lst = []
# s = 0
# for i in range(1,5):
#     user = int(input("inter your Number : "))
#     lst.append(user)
# for i in lst:
#     s = s + user
# print("append in list",lst)
# print("sum of all list number : ", s)



# wap to read list of size 10 and add even number in elements

# lst = []
# for i in range(1,11):
#     n = int(input("Enter a Number : "))
#     if n % 2 == 0 :
#         lst.append(n)
# print("Even number : ",lst)


# wap to read list of size 10 and add even or odd number in elements

# lst1 = []
# lst2 = []
# for i in range(1,11):
#     n = int(input("Enter a Number : "))
#     if n % 2 == 0 :
#         lst1.append(n)
#     else:
#         lst2.append(n)
# print("Even number : ",lst1)
# print("Odd number : ",lst2)


# wap to read list of size 10 and add possitive or negative number in elements

lst1 = []
lst2 = []
for i in range(1,11):
    n = int(input("Enter a Number : "))
    if n > 0 :
        lst1.append(n)
    elif n < 0:
        lst2.append(n)
print("possitive number : ",lst1)
print("Negative number : ",lst2)
