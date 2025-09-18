# Python is Object oreanted progamming 
# Almost everything in python  is a object

# Class - keyword use to create a classes
class myClass:
    x = 10

# create a object 
obj1 = myClass()
print(obj1.x)

# __init__() built in class method

# which always exe when class is being init 
# __init__() method use to assign the values of the class properties 

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("mitansh",20)
print(p1.name)
print(p1.age)

# The __init__() method is called automatically every time the class is being used to create a new object.


# __str__() - method controls what should be returned when the class is represented as a string
# if method is not set then the string representaion of the object is returned

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# create a methods inside class/ object its called functions 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


# self parameter is like a "this" keyword

# object parameter can be modify like this 
p1.age = 40

# del - keyword can use to delete object properties
del p1.age

# class can't be empty so we can avoid error by adding pass statment

