# Boolean Values - TRUE / FALSE -----------------------------

print(10 > 9)
print(10 == 9)
print(10 < 9)

# comparision return Boolean value in python
# if statment also return true and false

if 20 > 10:
    print("Yes it is")
    
# bool() can allow you to convert or assign any value to true and false

print(bool("Hello"))
x = 2
print(bool(x))

# almost any value evaluate true if it has any value 
# -> string is true , except empty string
# -> Any numbers are true , except 0
# -> list, tuple, disc are true , excpet empty one

# variables that eval as false - (),[],{},"",0,None,False
# class with a __len__ return 0 or false

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

# also function can return zero

