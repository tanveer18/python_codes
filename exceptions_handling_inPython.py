# try:
#     a = 5
#     c = a + b
#     print(c)
# except NameError as e:
#     print("Variable Error")
# except ValueError as e:
#     print("Value Error")



# try:
#     print("Start")
#     z = 4 / 2
#     print(z)
#
# except ZeroDivisionError:
#     print("Divid by Zero")
# except ValueError:
#     print("Value Error")
# else:
#     print("No Error")
# finally:
#     print("Always Execute")




# try:
#     print("Start")
#     z = 4 / 0
#     print(z)
#
# except ZeroDivisionError:
#     print("Divid by Zero")
# except ValueError:
#     print("Value Error")
# else:
#     print("No Error")
# finally:
#     print("Always Execute")




# def test():
#     try:
#         print("Start")
#         z = 4 / 0
#         print(z)
#     finally:
#         print("Close file")
#
#
# try:
#     test()
# except ZeroDivisionError:
#     print("Divid by Zero")
# except ValueError:
#     print("Value Error")
# else:
#     print("No Error")
# finally:
#     print("Always Execute")

try:
    age = int(input("Enter Your Age : "))
    if age < 0 :
        raise ValueError
    else:
        print("Age is Valid !")

except ValueError:
    print("The Age is Not Valid !")
