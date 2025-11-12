# Recursion is when we call a function within itself to solve smaller instances of the same problem. 


def countdown(n):
    if n <=0:
        print("Done")
    else:
        print(n)
        countdown(n-1) # calling the function with the n-1 value 

countdown(5)

# recurtion have 2 case :

# 1. A base case - A condition that stops recurtions
# 2. A Recursive case - the fuction calling itslef with midified arg

# without base case function call forever

# Factorial find 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) 
    
print(factorial(5))

# Fibonacci series
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

# recurtion using the list 
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:]) # getting all the values execept first elem 

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

# Recurtion depth limit - pythin have default 1000 limit

import sys
print(sys.getrecursionlimit())
