# inheritance allow us to define a class that inhertie all methods and properties from anoter class
# Parent class is the class being inherited from, also called base class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person): # inheriting the class Person
  pass

c = Student("mitansh", "patel")
c.printname()

