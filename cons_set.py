# class Set:
#     def __init__(self,x,y,z):
#         self.n1 = x
#         self.n2 = y
#         self.n3 = z
#     def sum(self):
#         s = self.n1 + self.n2 + self.n3
#         return s
#     def mean(self):
#         m = self.sum()/3
#         return m
#
# a =Set(2,5,3)
# b =Set(5,8,9)
# print("sum of set a is ",a.sum())
# print("mean of set a is ",a.mean())
# print("sum of set b is ",b.sum())
# print("mean of set b is ",b.mean())
#

str = int(input("Enter Your Number then i give area and circumferance : "))
class Circle:
    def __init__(self,n):
        self.redius = n
    def area(self):
        a = 3.14 * self.redius ** 2
        print("Area is : ",a)
    def circumference(self):
        c = 2 * 3.14 * self.redius
        print("Circumferance is : ",c)
a = Circle(str)
a.area()
a.circumference()


class workers:
    def __init__(self,x,y,z):
        self.Name = x
        self.Wages = y
        self.WorkingDays = z
    def ShowData(self):
        print("Name is : ",self.Name)
        print("Wages is : ",self.Wages)
        print("Working Days is : ",self.WorkingDays)
    def Payments(self):
        p = self.Wages * self.WorkingDays
        print("Payment is : ",p)
a = workers("veer",5000,25)
a.ShowData()
a.Payments()



