class Employee:
    def setData(self,n,s,a):
        self.Name = n
        self.Salary = s
        self.Advance = a
    def ShowData(self):
        print("Name is : ",self.Name)
        print("Salary is : ",self.Salary)
        print("Advance is : ",self.Advance)
    def Payments(self):
        p = self.Salary - self.Advance
        return p

a = Employee()
b = Employee()
a.setData("Raja",50000,20000)
b.setData("Amit",60000,10000)
a.ShowData()
print("Payments is ", a.Payments())
b.ShowData()
print("Payments is ", b.Payments())



