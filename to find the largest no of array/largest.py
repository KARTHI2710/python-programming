#to find largest number

def largestno(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                t=arr[i]
                arr[i]=arr[j]
                arr[j]=t
    return arr

def arraysort(arr):
    
    arr.sort()
    print(arr)
    print("largest number is : ",arr[len(arr)-1])

arr=[]
n=int(input("enter a no of array : "))
print("enter array elements ")
for i in range(n):
    v=int(input())
    
    arr.append(v)
#a=largestno(arr)
#print("largest number is  : ",a[len(a)-1])
arraysort(arr)
print(arr)

