# class methods vs. static methods - inheritance
class Pet: # base class
    _class_info = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about " + cls._class_info + "!")   
    
class Dog(Pet):
    _class_info = "man's best friends" # overload

class Cat(Pet):
    _class_info = "all kinds of cats" # overload
    
Pet.about()
Dog.about()
Cat.about()
