# class person:
#     def SetData(self,name,**informations):
#         self.SetData = name
#         self.SetData = informations
#     def ShowData(self):
#         print("Name is ",self.name)
#         for key , value in self.informations.items():
#             print(key, " is ", value)
# User = person()
# User.SetData(name = "Tanveer Khan",age = 44, city = "Amravati", Gender = "Male")
# User.ShowData()

# def display(*arguments):
#     print(arguments)
# display(45,2,3,6,7,78)
# display(46,2,13,86,71,8)
#
# def sum(*arguments):
#     s = 0
#     for i in arguments:
#         s = s + i
#     print("Sum of Number is : ",s)
# sum(45,2,3,6,7,78)
# sum(46,2,13,86,71,8)

# def even_number(*argument):
#     for i in argument:
#         if i % 2 == 0:
#             print("Even Number is : ",i)
# even_number(2,5,8,9,12,15,18,10)

#
# def display(Name,Roll_No,**Subjects):
#     print("Name is : ",Name)
#     print("Roll_No is : ",Roll_No)
#     s = 0;c =0
#     for key,value in Subjects.items():
#         print(key , " is :", value)
#     for key, value in Subjects.items():
#         s = s + value
#         c = c + 1
#     print("Sum of Total Marks : ",s)
#     percentage = s * 100 / (c * 100)
#     print("Percentage is :",percentage)
#     for key,value in Subjects.items():
#         if value < 40 :
#             print("Sorry Your Result is Fail!")
#             break
#     else:
#         print("Congratulation Your Result is Pass!")
# display("Zoyeb khan",10,Chemistry = 95,Physics = 95,Maths = 98,Biology = 85,English = 80)
# display("Zoyeb khan",15,Chemistry = 95,Physics = 35,Maths = 98,Biology = 85,English = 80)

def display(name,roll_no,**subjects):
    print("Name is :",name)
    print("Roll_No is :",roll_no)
    for key,value in subjects.items():
        print(key, "is", value)
    s = 0
    c = 0
    for key,value in subjects.items():
        s = s + value
        c = c + 1
    print("sum of all Subjects : ",s)
    percentages = s * 100 / (c * 100)
    print("Percentage is :",percentages)

    for key,value in subjects.items():
        if 40>value:
            print("Sorry Your Fail!")
            break
        else:
            print("Congradulation Your Pass!")
            break



display("Zoyeb khan",10,Chemistry = 95,Physics = 95,Maths = 98,Biology = 85,English = 80)



class box:
    def circle(self,l,b,h):
        a = l * b * h
        print("Area is ", a)

















