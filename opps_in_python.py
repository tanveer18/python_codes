class Students:
    def SetData(self,n,r,b,**m):
        self.Name = n
        self.Roll_Numbers = r
        self.Branch = b
        self.Marks = m
    def ShowData(self):
        print("Name is : ",self.Name)
        print("Roll Number is : ",self.Roll_Numbers)
        print("Branch is : ",self.Branch)
    def Total(self):
        t = 0
        for Mark in self.Marks:
            t = t + Mark
        print("Total Marks Is : ", t)
    def Result(self):
        for Mark in self.Marks:
            if Mark < 40:
                print("The Result Is Fail!")
                break
        else:
            print("Result is Pass!")


a = Students()
a.SetData("wasif",20,"Bca",45)
a.ShowData()
a.Total()
a.Result()




















