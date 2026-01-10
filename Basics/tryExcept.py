# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# can define as many except block we want
try:
    print("x") # x is not defined
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


# we can add else block that will execute if no errors were rised
else:
    print("Nothing went wrong")

# will work like normal finally block
finally: 
    print("will execute regadless if try raises an error or not")


# Real life usecase example
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
         f.close()
except:
    print("Something went wrong when opening the file")


# We can throw exeption by the keyword raise Exception
raise Exception("sorry, no number above zero")

# we can throw typeExecption by using raise typeError
raise TypeError("only integer values req")
