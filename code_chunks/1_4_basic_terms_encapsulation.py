# public, protected, private attributes 
class A():
    
    def __init__(self):
        self.__priv = "I am private" # inaccessible & invisible - can only be mutated inside the class definition
        self._prot = "I am protected" # should not be used outside of the class definition (unless in a subclass)
        self.pub = "I am public" # used freely inside/outside class definition
        
    def set_private_attribute(self, __priv):
        self.__priv = __priv
        
x = A()

print(x.pub)
x.pub = x.pub + " - changed freely!"
print(x.pub)

print(x._prot)

#x.__priv
