# pyhton have diffrent functions for working with file

# key function is open()

# 1. open()

# open function take two parameters filename and mode

# -r  READ default value, open a file for reading , error -> if the file does not exsitz
# -a Append open file for appending -> create new if doesn't exsist
# -w open a file for writing -> create new
# -x Create -> to create a file -> error if file with same name exist
# -t Text default value -> text mode
# -b Binary -> binray mode

f = open("demofile.txt")

f = open("default.txt", "rt") # same code 

# open file on server

f = open("demofile.txt")
print(f.read())

# we can also open file by file path
f = open("D:\\myfiles\welcome.txt")
print(f.read())


#  using with statement

with open("demoFile.text") as f:
    print(f.read())

# 2. close() -- to close the opened file

f = open("D:\\myfiles\welcome.txt")
print(f.read())

f.close()

# reading only parts of the file 
with open("demoFile.text") as f:
    print(f.read(5))


# 3. readline() -- use to read the first line of the file
f.readline()

# by calling readline() twise then we can get the first two line

# Looping through lines we can read whole file line by line

for x in f:
    print(x)


# Write to an existing file
# we can use two methods 
# 1. -a -> will write to the end of the file

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

# 2. -w -> will overwrite any existing content
with open("demofile.txt") as f:
  f.write("Now the file has more content!")

# W parameter will overwrite the whole file content 


# Remove file 

import os
os.remove("demofile.txt")

# check if file exist 

if os.path.exists("demofile.txt"):
   os.remove("demofile.txt")
else:
   print("file doesn't exsit")   

# delete folder 

os.rmdir("myfolder")
