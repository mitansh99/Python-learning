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



# slicing in String ------------------------------------

# -> use to get the range of char

# get the char from n to m - like 3 to 5
# it will not return the last char like we will get 3 and 4 char only
x = "hello world"
print(x[3:5])

print(x[:5]) # - slice from start to 5th char

print(x[3:]) # - slice from 3rd to end char

# can use nagativ indexing to start slicing from the end of the string
print(x[-5:-3])





