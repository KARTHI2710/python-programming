S=input("enter a string\n")
count=0
for char in S:
    if ("a" or "A") in char:
        count=count+1
    elif ("e" or "E") in char:
        count=count+1
    elif("i" or "I") in char:
        count=count+1
    elif("o" or "O") in char:
        count=count+1
    elif("u" or "U") in char:
        count=count+1
    else:
        count=count+0
print("no of vowels in the ",S,"is",count)
