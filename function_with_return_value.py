# Design a functions interest which will calculate and return simple interest from 3 arguments p,n,r?
def interest(p,n,r):
    simple_interest = p*n*r/100
    return simple_interest
p = interest(100000,10.45,5)
print("simple interest is : ",p)

# Design a functions volume which will return volume of box when lenght , breadth , and height is pass as argument?
#
# def volume(l,b,h):
#     Box_Volume = l * b * h
#     return Box_Volume
# print("Volume of Box : ",volume(20,15,32))

# Design a functions volume which will return volume of sphere when radius is pass as arguments

# def volume(r):
#     Volume_Sphere = 4/3*3.14*r**3
#     return Volume_Sphere
# Radius = int(input("Enter Radius Number : "))
# z = volume(Radius)
# print("Your Volume is :  ", z)


# Design a functions which will calculate and return factorial of  a no which in pass in arguments?

def factorial(n):
    f = 1
    for i in range(1 , n+1):
        f = f * i
    return f
z = factorial(5)
print("Your Factorial is : ", z)

# Design a function fact which will calculate and
# return factorial of a no. which is pass as argument.
# WAP to print factorial of all nos from 1 to 10
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
for a in range(1,21):
    print("Factorial of",a , "is ", factorial(a))

# Design a function isprime which will check if a number is prime or
# not and will return True or False

def Isprime(n):
    for i in range(1,n+1):
        if i % 2 == 0 :
            return False
        else:
            return True
a = int(input("Enter Your Number : "))
if Isprime(a):
    print(a, "Is Prime Number!")
else:
    print(a , "Is Not Prime Number!")