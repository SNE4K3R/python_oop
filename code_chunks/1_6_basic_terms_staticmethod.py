# class methods vs. static methods - inheritance

class Pet: # base class
    _class_info = "pet animals"

    @staticmethod
    def about():
        print("This class is about " + Pet._class_info + "!")   
    

class Dog(Pet):
    _class_info = "man's best friends" # overload
    
    #@staticmethod
    #def about(): # overlad --> define same function in subclass (redefinition)
    #    print("This class is about " + Dog._class_info + "!") 

class Cat(Pet):
    _class_info = "all kinds of cats" # overload
    
Pet.about()
Dog.about()
Cat.about()

# no way to differentate what kind of class it really is! 
