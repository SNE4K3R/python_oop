##--additional information--##

# python usually properties are used instead of private variables 
class P:

    def __init__(self,x): # member is public! 
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
            
p = P(1100)
print(p.get_x())
p.x = 1500 # it is still possible to reset the variable to a value higher than 1000! 
print(p.x)
print("-------")
    
class P:

    def __init__(self,x):
        self.x = x

    @property #python way! 
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
            
p = P(800)
print(p.x)
p.x = 1500 # can still set the variable public, but with specific constrains! 
print(p.x)
