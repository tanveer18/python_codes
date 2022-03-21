def display(p , n ,r):
    simple_interest = p * n * r /100
    print("Simple Interest Is : ",simple_interest)
amount = int(input("What is your Amount : "))
rate = float(input("What is your Rate : "))
year = int(input("What is your year : "))
display(p=amount,n=rate,r=year)
