# conditional case value
# wap to read salary and print grade according to given criteria ?
# salary                          grade
# >=50000                         A
# 25000 - 50000                   B
# 15000 - 25000                   C
# <15000                          D


salary = int(input("Enter Your Salary : "))
match salary:
    case salary>=50000:
        print("Your Grade is A")
    case salary>25000:
        print("Your Grade is B")
    case salary>15000:
        print("Your Grade is C")
    case_:
        print("Your Grade is D")