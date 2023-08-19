#to print sum of array

def sum_of_array(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    print("sum of array is ",sum)
    print("sum of array is "+str(sum))
    print("sum of array is {}".format(sum))
    print(f"sum of array is %d "%sum)

arr=[]
n=int(input("enter a no of array : "))
print("enter array elements ")
for i in range(n):
    v=int(input())
    
    arr.append(v)
sum_of_array(arr)
