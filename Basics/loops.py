# python have two types of loops

#  > while 
#  > for  

# loops are for exe same code until condition true


# while loop exe
i = 1
while i < 6:
  print(i)
  i += 1 # incrementing the number else loop become endless
  
# Break statment - use to stop teh execution of the loop

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue - statment used to stop the current itration and continue with next

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# else - statment we can use it run once when the condtion is no longer true

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
  
  
# For loops  - use to itrating over the sequence [], (), {},string

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# The for loop does not require an indexing variable to set beforehand.

# Even strings are iterable objects, they contain a sequence of characters

for x in "banana":
  print(x)
  
# range() - spacific numbers of times loop

for x in range(6):
  print(x)
  
# range ()'s default value is 0  - range(6) = 0,5


for x in range(2, 6):  # we can also spacify the starting index
    
    for x in range(2, 30, 3): # we can also spacify the increiment 
        
        print(x)

# range (staring index , ending index , incremnet) 

# else block will not going to exe when loop break through the break statment

# for loops can not be empty so..
# we can use the pass statment to avoid the error 

  
