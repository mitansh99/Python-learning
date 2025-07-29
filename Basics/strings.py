# Strings ---------------------------------

# string in python surrouned by the "" or '' ex. "hello" === 'hello'

# quote inside quote can be used by until they don't match
x = "hello 'world'" 

# -> multi-line string can be asign by the three quote - we can also use ''' '''
x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. """

# Strings are Arrays -------------------------------

# strings in python are array of the unicode characters
# python does not have any char data type - signle char is a string with length fo 1.
x = "Hello World"
print(x[2]) # l - start from 0

# Looping throught string - string is array so we can loop throught for loop

for x in "banana":
    print(x)
    
# String length - get length by the len()
x = "hello world"
print(len(x))

# check string - we can use "in" and "if" keyword to check the word present in string or not 

text = "this is my first python project"
print("first" in text) # return boolean
# or
if("first" in text):
    print("yes! it exsist")

# check if not - can be done using "not in"

text = "This is text"
print("is" not in text) # print bool - similer with if






