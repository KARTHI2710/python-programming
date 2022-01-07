a=100
name="karthi"
#normal printing
print("a = ",a,"name = ",name)
#using concatination
print("a = "+str(a)+" name = "+name)
#using str.format() method
print("a = {} name = {}".format(a,name))
#using str.format() position method
print("a = {0} name = {1}".format(a,name))
#using keyword argument in str.format() method
print("a = {v} name = {n}".format(v=a,n=name))
#using f or F before the string
print(f"a = {a} name = {name}") 

