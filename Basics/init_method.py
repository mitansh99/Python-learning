# All classes have built in method call __init__() 
# use to assign the values to the object

# __init__() == constructor of the class

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("Mitansh", 20)

print(f"my name is {p1.name} and i am {p1.age} years old")


