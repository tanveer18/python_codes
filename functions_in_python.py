# # wap a functions to print all numbers 1 to 100?
# def display():
#     for i in range(1,101):
#         print(i, end=" ")
# # display()
#
# # wap a functions to print all even numbers to 1 to 100?
# def even():
#     for i in range(1,101):
#         if i % 2 == 0:
#             print(i , end=" ")
#
# even()
#
# # even functions to write other types
# def even2():
#     for i in range(2,101,2):
#         print(i)
# even2()
#
# # wap a programme to print star
# def star():
#     for i in range(1,51):
#         print("*", end="")
# print("ccit")
# star()
# print("\nAmravati")
# star()
# print("\npython")
# star()
#
# # Designed a funtion odd which will print all even number in range 1 to 100
# def odd():
#     for i in range(1,101):
#         if i% 2!=0:
#             print(i, end="")
# odd()
#


# Designed a function sphere which will read radius and will calculate and print volume of sphere

s = int(input("Enter Your Radius : "))
def sphere(s):
    v = 4/3*3.14*s**3
    print(v)
sphere()
