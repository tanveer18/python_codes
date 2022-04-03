class person:
    def __init__(self,n,c,a):
        self.name = n
        self.city = c
        self.age = a
    def showdata(self):
        print("Name is : ",self.name)
        print("City is : ",self.city)
        print("Age is : ",self.age)
a = person("wasif","Amravati",22)
b = person("Aabid","Paratwada",21)
c = person("Shreyash","Nagpur",23)
d = person("Vivek","Pune",25)
e = person("Zakir","Hydrabad",30)
lst = [a,b,c,d,e]
print("First Data")
a.showdata()
print("Second Data")
b.showdata()
print("Third Data")
c.showdata()
print("Fourth Data")
d.showdata()
print("Five Data")
e.showdata()
s = 0
for obj in lst:
    s = s + obj.age
m = s / len(lst)
print("Average age is : ", m)
