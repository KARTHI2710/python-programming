class Example:
    common=50    #class variable
    def sample(self,arg):
        self.i=arg   # i is instanace variable
a=Example()
b=Example()
a.sample(10)
b.sample(20)
print(a.common,a.i)
print(b.common,b.i)
