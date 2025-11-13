# Json is a inbuilt module use to play with json data

import json

# parse json - convert json -> to python 
x = '{"name" :"mitansh", "age": 19}'

python_dict = json.load(x) # convert to the pyhton dictionary


python_Code = {
    "name": "mitansh", 
    "age": 19
}

json_string = json.dump(python_Code) # converting the python dict -> json obj


# Can convert this much python data type into the json obj 
print(json.dumps({"name": "John", "age": 30}))# - json obj
print(json.dumps(["apple", "bananas"])) # - Array
print(json.dumps(("apple", "bananas"))) # - Array
print(json.dumps("hello")) # str
print(json.dumps(42))# - number
print(json.dumps(31.76))# - number
print(json.dumps(True))# - true
print(json.dumps(False))# - false
print(json.dumps(None))# - null

# indent - parameter in dumps() to make it readable

json_string = json.dump(python_Code , indent=4)

# seprators = (",",":") -default format for json obj 

json_string = json.dump(python_Code, separators=(".", "=")) # custom format 

# sort_keys= true - paramert can be use to sort the json object bases of key

json_string = json.dump(python_Code, sort_keys=True) # now obj will be sort by the keys
