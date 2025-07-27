# creating variables - No command for declareing a Variable.
# created at moment when firssr assign a value to it.

x = 5
y = "Mitansh"

# Do not declare with perticuler type - can even change after they have been set,

a = 4
a = "hello !"

# Spacify the datatype with help of casting

b = str(3) # b will be the '3'

# variables type can be get by the type() function

# string can be define by the single & double quotes

s = "jhone"
s = 'jhone' #both are the same

#variable name is case sensitive 

m = "hello"
M = 23 #both is diffrent variables with diffrent values

#------------------------------- Variable names --------------------------------

# Start with _ char
# Can not start with numbers
# contian only alpha numeric char & __ 
# varibale names are casesensitive
# can not be any python keyword

# 2myvar = "Jhone"
# my-var = "John"
# mu Var = "John"

myVariableName = "Mitansh" # camel case

MyVariableName = "Mitansh" # pascal case

my_variable_name = "Mitansh" # snake case

#------------------------ Variable-Assign Multiple values -----------------------

# Allow in python - assign multi value to multi var
x,y,z = "Orange", "banana", "cherry"

# single value to multi var
x = y = z = "orange"

# unpack collection,list,tuple
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits

#------------------------ Variable-Assign Multiple values -----------------------

# In python print() ofthen use to output variables
a = "hello !"
print(a)

# multi var can be seprated by comma in sinle print()
x = "hello"
y = "world"
z = "!"
print(x,y,z)

# we can also use + operator 
print(x+y+z) # for numbers + will work as mathematical operator

# string and number can not be concat with the +


#------------------------ Global Variables -----------------------

# Variables which is define outside the function is a global var

# gloabl key word - to make function local variable global

def myFunction():
    global a 
    a = "Hello"
myFunction()

print(a)


