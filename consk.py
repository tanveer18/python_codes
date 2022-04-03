# class Box:
#     def __init__(self,l ,b,h):
#         self.lenght = l
#         self.breath = b
#         self.height = h
#     def Volume(self):
#         v = self.lenght * self.breath * self.height
#         print("volume of Box : ", v)
#
# a = Box(5,6,4)
# a.Volume()
# b  = Box(8,7,9)
# b.Volume()



class Circle:
    def __init__(self,r):
        self.Redius = r
    def area(self):
        a = 3.14 * self.Redius ** 2
        print("Area is : ",a)
    def circumerence(self):
        c = 2 * 3.14 * self.Redius
        print("Circumference is : ",c)
a = Circle(5)
a.area()
a.circumerence()
