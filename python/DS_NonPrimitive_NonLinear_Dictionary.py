# **********************************************************************************************************************************************************************
# DICTIONARY - OPERATOR
# **********************************************************************************************************************************************************************
dictionary = {"name": "Hello", "age": 10}
print(f"Operator = - Assignement: {dictionary}")
dictionary |= {"high": 170}
print(f"Operator |= - Update assignement different dictionaries: {dictionary}")
merged_dict = dictionary | {1: 2}
print(f"Operator | - Merge/Union different dictionaries: {merged_dict}")
if dictionary != {1: 2}:
    print("Operator ==/!= - Compare equality dictionaries:")
if "name" in dictionary:
    print("Operator in - Check if a key in dictionary:")
print("***************************************************************************************************************************************************************")
# **********************************************************************************************************************************************************************
# DICTIONARY - METHOD
# **********************************************************************************************************************************************************************
print(f"Method get - Return the value for key: {merged_dict.get("name")}")
print(f"Method keys - Return key list: {merged_dict.keys()}")
print(f"Method values - Return value list: {merged_dict.values()}")
print(f"Method items - Return (key, value): {merged_dict.items()}")
merged_dict.update({"color":"red"})
print(f"Method update - Append a dictionary: {merged_dict}")
merged_dict.popitem()
print(f"Method popitem -  Remove and return last key, value: {merged_dict}")
merged_dict.pop(1)
print(f"Method pop -  Remove and return item at a key: {merged_dict}")
shallow_dict = merged_dict.copy()
print(f"Method copy -  Shallow copy a dictionary: {shallow_dict}")
new_dict = merged_dict.fromkeys(["age"],20)
print(f"Method fromkey -  Create a new dictionary from founded key list with set value: {new_dict}")
default_dict = merged_dict.setdefault("hobby","game")
print(f"Method setdefault -  Return value of a key if it exists. If not, insert key and value: {default_dict}")
print("***************************************************************************************************************************************************************")
# **********************************************************************************************************************************************************************
# DICTIONARY - BUILT-IN FUNCTION
# **********************************************************************************************************************************************************************
print(f"Built-in function len(...) - Return the number of key-value pairs: {len(merged_dict)}")
print(f"Built-in function str(...) - Return a string representation: {str(merged_dict)}")
print(f"Built-in function type(...) - Return the type of class dictionary: {type(merged_dict)}")
print(f"Built-in function dict(...) - Create a new dictionary: {dict(a=1,b=2)}")
print(f"Built-in function sorted(...) - Return a sorted list of the dictionary's keys: {sorted(merged_dict)}")
print(f"Built-in function all(...) - Return True if all keys are truthy: {all(merged_dict)}")
print(f"Built-in function any(...) - Return True if any key is truthy: {any(merged_dict)}")
print("***************************************************************************************************************************************************************")
# **********************************************************************************************************************************************************************
# DICTIONARY - DATA STRUCTURE
# **********************************************************************************************************************************************************************
# Create a dictionary                                                                                                                           # Time - Space
#
# Solution 1: Using assignement operator                                                                                                        # O(n) - O(n)
dict_1 = {"A": 1, "B": 2}
print(f"DS - Create a dictionary - Solution 1: {dict_1}")
# Solution 2: Using dictionary comprehension                                                                                                    # O(n) - O(n)
dict_2 = {f"{x}": x**2 for x in range(10)}
print(f"DS - Create a dictionary - Solution 2: {dict_2}")
# Solution 3: Using dictionary comprehension with list                                                                                          # O(n) - O(n)
list = [1, 2, 3]
dict_3 = {"E": item for item in list}
print(f"DS - Create a dictionary - Solution 3: {dict_3}")
# Solution 4: Using dictionary comprehension with dictionary                                                                                    # O(n) - O(n)
dict_4 = {"E": item for (key, item) in dictionary.items() if key == "name"}
print(f"DS - Create a dictionary - Solution 4: {dict_4}")
# Solution 5: Using dictionary constructor                                                                                                      # O(n) - O(n)
dict_5 = dict([("foo", 100), ("bar", 200)])
print(f"DS - Create a dictionary - Solution 5: {dict_5}")
# Solution 6: Using dictionary constructor                                                                                                      # O(n) - O(n)
dict_6 = dict(foo=100, bar=200)
print(f"DS - Create a dictionary - Solution 6: {dict_6}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Access a value in a dictionary                                                                                                                 # Time - Space
#
# Solution
print(f"DS - Access a value in a dictionary - Solution: {dict_1["A"]}")                                                                          # O(n) - O(1)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Traverse values in a dictionary                                                                                                                # Time - Space
#
# Solution:                                                                                                                                     # O(n) - O(1)
def traverse_dict(dictionary):
    for key in dictionary:
        print(f"\t{dictionary[key]}")
print("DS - Traverse values in a dictionary - Solution:")
traverse_dict(dictionary)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Update a value of key in a dictionary                                                                                                         # Time - Space
#
# Solution:                                                                                                                                     # O(1) - O(n)
dictionary["high"] = 90
print(f"DS - Update an value of key in a dictionary - Solution: {dictionary}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Insert key and value in a dictionary                                                                                                           # Time - Space
#
# Solution:                                                                                                                                     # O(1) - amortized O(1)
dictionary["low"]=10
print(f"DS - Insert key and value in a dictionary - Solution: {dictionary}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Search a value in a dictionary                                                                                                                # Time - Space
#
# Solution:                                                                                                                                     # O(n) - O(1)
def search_item_dict(dictionary,item):
    for key in dictionary:
        if dictionary[key] == item:
            return key,item
    return "The value can not found"
print(f"DS - Search a value in a dictionary - Solution: {search_item_dict(dictionary,"Hello")}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Delete key and item in a dictionary                                                                                                           # Time - Space
#
# Solution 1: Using pop method                                                                                                                  # O(1) - O(1)
dict_2.pop("0")
print(f"DS - Delete key and value in a dictionary - Solution 1: {dict_2}")
# Solution 2: Using popitem method                                                                                                              # O(1) - O(1)
dict_2.popitem()
print(f"DS - Delete key and value in a dictionary - Solution 2: {dict_2}")
# Solution 3: Using delete function                                                                                                             # O(n) - O(1)
del(dict_2["1"])
print(f"DS - Delete key and value in a dictionary - Solution 3: {dict_2}")
# Solution 4: Using clear method                                                                                                                # O(n) - O(1)
dict_2.clear()
print(f"DS - Delete key and value in a dictionary - Solution 4: {dict_2}")
