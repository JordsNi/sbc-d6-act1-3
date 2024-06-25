#BINI Logo (Activity 3)

ask = int(input("Enter a Number: "))
for i in range(ask,0,-1):
    space = ask - 2
    if i == 1:
        print("*"* i+" " * space+"*"*i)
    else:
        print("*" * i)
for j in range(2,ask+1):
    print("*" * j)