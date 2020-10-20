# class methods vs. static methods - inheritance

class Pet: # base class
    _class_info = "pet animals"

    def about(self):
        print("This class is about " + self._class_info + "!")   

class Dog(Pet):
    _class_info = "man's best friends" # overload

class Cat(Pet):
    _class_info = "all kinds of cats" # overload
    
p = Pet()
p.about()
d = Dog()
d.about()
c = Cat()
c.about()

# works, but from the design point of few it is bad to always have to make
# a class object to know what kind of class it is.
