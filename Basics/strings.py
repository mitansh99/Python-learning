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

# string modifications ---------------------------------

# buit in methods to modify string 

"hello world".upper() # to convert string to the upper case

"hello world".lower() # to covert string to the lower case

"hello world".strip() # to remove whitespace from the string

"hello world".replace("h" , "k") # to replace strig with other string 

"hello world".split(" ") # split string from the given string return array


# String Concatenation  -----------------------------------

# concate or combine two string by using '+'

x = "hello"
y = "world"
print(x + y)

print(x + " " + y) # to add space between concate

# f-string  ----------------------------------

# As we can not do "hello" + 10 so we can use f - format() method to combine the string with numbers

age = 15
text = f"Hello world ! {age}" # can be use as place holder or modifer

# place holder can include modifer to format 

price = 10
text = f"price of this product is {price:.2f}" # convert to the 2 decimal points 10.00

# place holder can contain the python code 
gst = 2
text = f"price is {price * gst}"


# Escape character ---------------------------------------

# use to add the char that are illegal in the string - \
text =  "we are \"gammers\" from india"

# \' - single quote 
# \\ - Backslash
# \n - New line
# \r - carriage return
# \t - tab
# \b - backspace
# \f - form feed
# \ooo - Octal view
# \xhh - Hex view

print("hello word lakhi de")




