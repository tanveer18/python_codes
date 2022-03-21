class workers:
    def __init__(self,n,w,wday):
        self.Name = n
        self.Wages = w
        self.Working_Days = wday
    def ShowData(self):
        print("Name is :",self.Name)
        print("Wages is : ",self.Wages)
        print("Working Days is :",self.Working_Days)
    def Payment(self):
        P = self.Wages * self.Working_Days
        print("Payment is : ", P)
a = workers("Raja",500,20)
a.ShowData()
a.Payment()
