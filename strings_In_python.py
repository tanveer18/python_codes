# format string contains curly braces{} as placeholder or replacement fields which gets replaced
a = 5
b = 20
s = "value are {} and value {}"
x = s.format(a,b)
print(x)

c = "python is high level language and good for beginners"
print(c.index('go'))

# count function is find the total user given strings
print(c.count(c))

# lenght function find the lenght of user given strings
print(len(c))
co = 0
for i in c:
    co = co + 1
print(c)

a1 = "welcome to the python"
b1 = "amravati"
s1 = "tanveer %s %s "%(a1,b1)
print(s1)
st = "%s %f "%("java ",3.0)
print(st)
