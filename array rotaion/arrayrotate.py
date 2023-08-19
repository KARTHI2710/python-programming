#Array rotation

arr=[]
n=int(input("enter a no of array : "))
print("enter array elements ")
for i in range(n):
    v=int(input())
    arr.append(v)

value=int(input("enter no of value to shift left : "))


for i in range(0,value):
    t=arr[0]
    for j in range(0,len(arr)-1):
        arr[j]=arr[j+1]
    arr[len(arr)-1]=t

print(arr)
