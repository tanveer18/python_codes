# def print_functions(a,b,c,d):
#     print(a,b,c,d)
# print_functions("tanveer","wasif","aabid","shreyash")


def funargs(normal, *args, **kwargs):
    # print(type(kwargs))
    print(normal)
    # print(type(args))
    # print(args)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(f"key is {key} and value is {value}")
veer = ["tanveer","wasif","aabid","shreyash"]
normal = "this is a normal value"
kw = {"tanveer":"programmer","wasif":"hadoop","aabid":"java developer","shreyash":"bussiness"}
funargs(normal, *veer,**kw)
