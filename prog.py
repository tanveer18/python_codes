# Wap to count all number negative a list
lst  = []
c = 0
for i in range(1,11):
    n = int(input("Enter a No : "))
    lst.append(n)
print("list in : ",lst)
for i in lst:
    if i > 0:
        print("Number is possitive")
else:
    print("Number is negative")