# wap to read list of size 10 and find the sum all elements.
lst = []
for i in range(1,11):
    n = int(input("Enter a No : "))
    lst.append(n)
print(lst)
s = 0
for i in lst:
    s = s + i
print("sum of ", s)

# wap to read 10 and create list of even number
lst1 = list()
for i in range(1,11):
    n = int(input("Enter a No : "))
    if n % 2 == 0:
        lst1.append(n)
print("Even number in List : ",lst1)



