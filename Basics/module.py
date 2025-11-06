# Module - same code as a code lib
# is a file containing the set of functions you want to include in your application.

# just save file with .py extension
def greeting(name):
  print("Hello, " + name)
# This is code for module.py file.


# how to import module

import mymodule ## -- assuming mymodule.py is the file name

mymodule.greeting("Jonathan")

# module can contain variables as well arrays,dict,objects etc

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# how to use it in other file

a = mymodule.person1["age"]
print(a)

import mymodule as mx # as keyword use to give module an alias name

# python have some built in module as well
# like platform,math,random etc

from mymodule import person1 # from keyword use to import specific thing from module