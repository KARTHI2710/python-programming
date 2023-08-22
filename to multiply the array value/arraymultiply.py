l=[]
n=int(input("enter no of values : "))
print("enter the values one by one")
sum=1
for i in range(0,n):
    v=int(input())
    l.append(v)
    sum=sum*v
d=int(input("enter the divisible number : "))
print(sum)
m=sum%d
print(l)
print(m)
