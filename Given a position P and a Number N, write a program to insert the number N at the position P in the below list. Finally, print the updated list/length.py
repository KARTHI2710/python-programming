
numbers = [10, 20, 30, 40, 50]
#Write your code here
P=int(input())
N=int(input())
#length=len(numbers)
if P<0 or P>len(numbers):
    print("Invalid")
else:
    numbers.insert(P,N)
    print(numbers)
