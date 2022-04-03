# two way to create a list
# this way to first empty list create
lst = list()


# append funtions add an element at the end of the list

lst2 = [10,50,60,30]
lst2.append(40)
print(lst2)

# copy function return a copy of the list
lst3 = lst2.copy()
print(lst3)

# count function return the number of elements with the specified value
print(lst2.count(50))

lst4 = ["tanveer","wasif","aabid"]
lst5 = ["shreyash","adnan","mayur"]
"""index function return the index of the first element with the specified value.if not found an valueError 
Exception will be throw"""
print(lst4.index('aabid'))

fruits = ['apple','banan','mango']
# insert function add an element at the specified positions
fruits.insert(2,'orange')
print(fruits)

# pop function remove the first item with the specified value
fruits.pop(1)
print(fruits)

# remove function removes the first item with the specified value

fruits.remove('apple')
print(fruits)

# reverse functions reverses the order of the list
fruits.reverse()
print(fruits)


# sort functions sort the list by alphabetical
fruits.sort()
print(fruits)


# wap to read list of size 10 and display

lst10 = list()
for i in range(1,11):
    n = int(input("Enter a no : "))
    lst.append(n)
    lst.sort()
print(lst)