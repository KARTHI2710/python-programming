#Array rotation

arr=[]
n=int(input("enter a no of array : "))
print("enter array elements ")
for i in range(n):
    v=int(input())
    arr.append(v)

value=int(input("enter no of value to shift left : "))
sub=[]
for i in range(0,value):
    sub.append(arr[i])
newarr=[]
for i in range(value,len(arr)):
    newarr.append(arr[i])
print(newarr+sub)

