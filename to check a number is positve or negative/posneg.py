def check(num):
    if num==0:
        print("neither positive nor negative")
    elif num<0:
        print("Negative")
    else:
        print("Positive")
num=int(input("enter a number\n"))
check(num)
a=int(input("enter a number\n"))
check(a)
