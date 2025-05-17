# **********************************************************************************************************************************************************************
# TUPLE - OPERATOR
# **********************************************************************************************************************************************************************
tuple_op = (1, 2, 3, 4)
print(f"Operator = - Assignment: {tuple_op}")
print(f"Operator == != etc. - Compare 2 tuples lexicographically: {tuple_op != (8,9)}")
print(f"Operator [] - Index: {tuple_op[1]}")
print(f"Operator [:] - Slice tuple: {tuple_op[2:]}")
print(f"Operator + - Combine 2 tuples into a new tuple: {tuple_op + (5,6,7)}")
print(f"Operator * - Repeat the tuple with the number of times: {tuple_op * 2}")
if 3 in tuple_op:
    print("Operator in/not in - Check if the item is present in tuple")
print(
    "***************************************************************************************************************************************************************"
)
# **********************************************************************************************************************************************************************
# TUPLE - METHOD
# **********************************************************************************************************************************************************************
print(
    f"Method count(...) - Return the number of times item appears in tuple: {tuple_op.count(2)}"
)
print(
    f"Method index(...) - Return the index of the 1st occurrence of item: {tuple_op.index(1)}"
)
print(
    "***************************************************************************************************************************************************************"
)
# **********************************************************************************************************************************************************************
# TUPLE - BUILT-IN FUNCTION
# **********************************************************************************************************************************************************************
print(
    f"Built-in function len(...) - Return the number of items in tuple: {len(tuple_op)}"
)
print(f"Built-in function max(...) - Return the maximum item: {max(tuple_op)}")
print(f"Built-in function min(...) - Return the minimum item: {min(tuple_op)}")
print(
    f"Built-in function sum(...) - Return the sum of all numeric item: {sum(tuple_op)}"
)
print(f"Built-in function sorted(...) - Return a new sorted tuple: {sorted(tuple_op)}")
print("Built-in function reversed(...) - Return a reversed iterator:")
for item in reversed(tuple_op):
    print("\t" + str(item))
print("Built-in function enumerate(...) - Return index item pairs:")
for index, item in enumerate(tuple_op, start=1):
    print("\t" + str(index) + " " + str(item))
print(
    f"Built-in function any(...) - Return True if at lest 1 item is truthy: {any(tuple_op)}"
)
print(
    f"Built-in function all(...) - Return True if all items are truthy: {all(tuple_op)}"
)
print(f"Built-in function tuple(...) - Create a new tuple: {tuple([1,2])}")
print(f"Built-in function count(...) - Count times item appears: {tuple_op.count(4)}")
print(
    f"Built-in function index(...) - Return index of the 1st occurrence of item: {tuple_op.index(4)}"
)
# **********************************************************************************************************************************************************************
# TUPLE - DATA STRUCTURE
# **********************************************************************************************************************************************************************
# Create a tuple                                                                                                                                # Time - Space
#
# Solution 1:                                                                                                                                   # O(1) - O(n)
tuple_1 = (1, 2, 3)
print(f"DS - Create a tuple - Solution 1: {tuple_1}")
# Solution 2: Using tuple built-in function                                                                                                     # O(1) - O(n)
tuple_2 = tuple("abcdef")
print(f"DS - Create a tuple - Solution 2: {tuple_2}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Access an item in a tuple                                                                                                                     # Time - Space
#
# Solution:
print(f"DS- Access an item in a tuple - Solution: {tuple_1[1]}")                                                                                # O(1) - O(1)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Traverse items in a tuple                                                                                                                     # Time - Space
#
# Solution:                                                                                                                                     # O(n) - O(1)
def traverse_item_tuple(tup):
    for item in tup:
        print(f"\t{item}")
print("DS - Traverse items in a tuple - Solution:")
traverse_item_tuple(tuple_1)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Search an item in a tuple                                                                                                                     # Time - Space
#
# Solution 1:                                                                                                                                   # O(n) - O(1)
def search_item_tuple(tup,item):
    for value in tup:
        if value == item:
            return "Found item"
    return "Not Found"
print(f"DS - Search an item in a tuple - Solution 1: {search_item_tuple(tuple_2,"a")}")
# Solution 2: Using in operator                                                                                                                 # O(n) - O(1)
print(f"DS - Search an item in a tuple - Solution 2: {"a" in tuple_2}")
# Solution 3: Using index method                                                                                                                # O(n) - O(1)
print(f"DS - Search an item in a tuple - Solution 3: {tuple_2.index("a")}")
