# funtions - methods() 

# functions is a block of code that is run when it call - to avoid code repitation 

# def - key word to define or create a function

def my_firstFunction(): # creation - defination of function 
    print("Hello")


my_firstFunction() # function calling

# information or the input for the function is known as arguments/parametrs

def fun_with_args(name):
    print("my name is ", name)

fun_with_args("mitansh")


# in python function must be call with the req number of args otherwise will get error

# Arbitrary Arguments, *args - add * if you dont know how manay number of args gonaa come

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# this is called keyword args

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

# Arbitrary Keyword Arguments, **kwargs 
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# default parameter value 

# if we dont get any value as arg then default value become the current value that is use to avoid errors

def my_function(country = "Norway"):
  print("I am from " + country)
  
  
# Return Values
# To let a function return a value, use the return statement:

def ret_fun():
    return 2+2

# pass - in python function can't become empty so we have to use pass satment to avouid the erros
