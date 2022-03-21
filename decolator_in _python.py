# class sphere:
#     def setRedius(self,n):
#         self.Redius = n
#     def Volume(self):
#         V = 4/3 * 3.14 * self.Redius ** 3
#         print("Volume is ", V)


class working:
    def setData(self,n,s,d):
        self.Name = n
        self.Salary = s
        self.Working_days = d
    def ShowData(self):
        print("Name is : ", self.Name)
        print("Salary is : ", self.Salary)
        print("Working Days is : ", self.Working_days)
    def Payment(self):
        P = self.Salary * self.Working_days
        return P
A = working()
B = working()
A.setData("Tanveer",100000,5)
B.setData("Raheel",50000,8)
A.ShowData()
print("Total salary is : ", A.Payment())
B.ShowData()
print("Total salary is : ", B.Payment())
Z = A.Payment() + B.Payment()
print("Total Payment is : ", Z)

