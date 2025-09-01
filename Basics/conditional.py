# if use to check the condtion if it is true then exe block of code
b = 10
a = 5 

if b > a:
    print("b is greater")

    
# use indentation insted of the brakets

# elif - if constion is fail then try this one 

if b > a:
  print("b is greater than a")
elif a == b:  # first condition is not true
  print("a and b are equal")
  
  
# else - cathch anything which isn't caught un the preceding conditions
  
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
# short hand if

if a > b: print("a is greater than b")

# short hand if else
print("A") if a > b else print("B")

# This technique is known as Ternary Operators, or Conditional Expressions.

# and operator to connect 2 conditions if a > b and c > a:

# or condition exe if one of condition is true if a > b or a > c:

# not reverse the result if not a > b:

# match statment - solution of the if else ladder

# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
    
  case 1 | 2 | 3 | 4 | 5: # combined values
    print("Today is a weekday")
  case _:  # its last case == else
    print("Looking forward to the Weekend")