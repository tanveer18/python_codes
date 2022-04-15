class Rectangle:
    def setdimension(self,x,y):
        self.breath = x
        self.lenght = y
    def area(self):
        a = self.breath * self.breath
        print("Area is : ",a)
class circle:
    def setredius(self,n):
        self.redius = n
    def area(self):
        a = 3.14 * self.redius ** 2
        print("Area is : ",a)
def display(n):
    for i in range(1 , n+1):
        print(i)