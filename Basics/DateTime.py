# to work with date time we have to import datetime module
# python have not an in built date time class
import datetime

# now() method of datetime class return current date and time
x = datetime.datetime.now()
print(x) # ouput- 2025-11-06 05:42:48.675418

print(x.year) # ouput- 2025
print(x.month) # ouput- 11
print(x.day) # ouput- 6
print(x.hour) # ouput- 5
print(x.minute) # ouput- 42
print(x.second) # ouput- 48

# creating date object
y = datetime.datetime(2020,5,17) # requires year,month,day
print(y) # ouput- 2020-05-17 00:00:

# strftime() method - to format date time object to string
print(x.strftime("%A")) # ouput- Wednesday
print(x.strftime("%B")) # ouput- November
print(x.strftime("%Y")) # ouput- 2025
print(x.strftime("%I")) # ouput- 05
print(x.strftime("%p")) # ouput- AM
print(x.strftime("%f")) # ouput- 675418
print(x.strftime("%c")) # ouput- Wed Nov  6 05:42:48 2025
print(x.strftime("%x")) # ouput- 11/06/25
print(x.strftime("%X")) # ouput- 05:42:48