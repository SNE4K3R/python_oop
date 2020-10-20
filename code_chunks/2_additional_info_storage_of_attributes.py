##--additional information--##

# class attributes 
class A:
    a = "I am a class attribute!"

x = A()
y = A()
print(x.a)
print(y.a)
print(A.a)
print("-------------------")

x.a = "This creates a new instance attribute for x"

print(x.a)
print(y.a)
print(A.a)
print("-------------------")

A.a = "This is changing the class attribute"

print(x.a)
print(y.a)
print(A.a)
print("-------------------")

# Python's class attributes and object attributes are stored in separate dictionaries
print(x.__dict__) # instances dictionary
print("-------------------")
print(x.__class__.__dict__) # class dictrionary
print("-------------------")
print(A.__dict__)
