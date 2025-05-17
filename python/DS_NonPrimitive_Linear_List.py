# **********************************************************************************************************************************************************************
# LIST - OPERATOR
# **********************************************************************************************************************************************************************
list_ex = [1, 2, 3, 4, 5, 6, 7]
print(f"Operator = - Assignement: {list_ex}")
list_ex += [10, 11]
print(f"Operator += - Augmented assignment: {list_ex}")
if list_ex != [3, 4]:
    print("Operator == >= etc. - Comparison")
print(f"Operator [] - Index: {list_ex[1]}")
print(f"Operator [:] - Slice list: {list_ex[1:]}")
print(f"Operator + - Concatenation 2 lists: {list_ex + [8,9]}")
print(f"Operator * - Multiply a list with a times: {list_ex * 3}")

if 3 in list_ex:
    print("Operator in - Check if the item is present in list")
print(
    "***************************************************************************************************************************************************************"
)
# **********************************************************************************************************************************************************************
# LIST - METHOD
# **********************************************************************************************************************************************************************
list_ex.append(4)
print(f"Method append - Add an item at the end: {list_ex}")
list_ex.extend([4, 5, 6, 7])
print(f"Method extend - Extend all items in list: {list_ex}")
list_ex.insert(6, 4)
print(f"Method insert - Insert an item at index: {list_ex}")
list_ex.remove(4)
print(f"Method remove - Remove the first item: {list_ex}")
list_ex.pop(2)
print(f"Method pop - Remove the item at index: {list_ex}")
list_ex_2 = [1, 2]
list_ex_2.clear()
print(f"Method clear - Remove all items from list: {list_ex_2}")
index_value = list_ex.index(4, 1, 5)
print(f"Method index - Return first index item from start to end index: {index_value}")
count_value = list_ex.count(4)
print(f"Method count - Return the number of item appears in list: {count_value}")
list_ex.sort()
print(f"Method sort - Sort items in list: {list_ex}")
list_ex.reverse()
print(f"Method reverse - Reverse items in list: {list_ex}")
list_copy = list_ex.copy()
print(f"Method copy - Return a shallow copy list: {list_copy}")
print(
    "***************************************************************************************************************************************************************"
)
# **********************************************************************************************************************************************************************
# LIST - BUILT-IN FUNCTION
# **********************************************************************************************************************************************************************
print(
    f"Built-in function len(...) - Return the number of items in list: {len(list_ex)}"
)
print(f"Built-in function max(...) - Return the lagest item: {max(list_ex)}")
print(f"Built-in function min(...) - Return the smallest item: {min(list_ex)}")
print(
    f"Built-in function sum(...) - Return the sum of all numeric item: {sum(list_ex)}"
)
print(f"Built-in function sorted(...) - Return a new sorted list: {sorted(list_ex)}")
print("Built-in function reversed(...) - Return a reversed iterator:")
for item in reversed(list_ex):
    print("\t" + str(item))
print("Built-in function enumerate(...) - Return index item pairs:")
for index, item in enumerate(list_ex, start=1):
    print("\t" + str(index) + " " + str(item))
print(
    f"Built-in function any(...) - Return True if at lest 1 item is truthy: {any(list_ex)}"
)
print(
    f"Built-in function all(...) - Return True if all items are truthy: {all(list_ex)}"
)
print(f"Built-in function list(...) - Create a new list: {list((1,2))}")
print(f"Built-in function count(...) - Count times item appears: {list_ex.count(4)}")
print(
    f"Built-in function index(...) - Return index of the 1st occurrence of item: {list_ex.index(4)}"
# **********************************************************************************************************************************************************************
# LIST - DATA STRUCTURE
# **********************************************************************************************************************************************************************
# Create a list                                                                                                                             # Time - Space
#
# Solution 1:                                                                                                                               # O(n) - O(n)
list_1 = [1, 2, 3]
print("DS - Create a list - Solution 1: \n\t{}".format(list_1))
# Solution 2: List Comprehension                                                                                                            # O(n) - O(n)
list_2 = [x for x in list_1]
print("DS - Create a list - Solution 2: \n\t{}".format(list_2))
# Solution 3: Conditional List Comprehension                                                                                                # O(n) - O(n)
list_3 = [x for x in list_1 if x < 3]
print("DS - Create a list - Solution 3: \n\t{}".format(list_3))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Access an element in a list                                                                                                               # Time - Space
#
# Solution:                                                                                                                                 # O(1) - O(1)
def access_element_list(list, index):
    if index >= len(list):
        print("\tOut of range of list")
    else:  # O(1) - O(1)
        print("\tDetect: {}".format(list[index]))


print("DS - Access an element in a list - Solution:")
access_element_list(list_1, 2)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Traverse elements in a list                                                                                                               # Time - Space
#
# Solution:                                                                                                                                 # O(n) - O(1)
def traverse_list(list):
    for element in list:
        print("\t{}".format(element))


print("DS - Traverse elements in a list - Solution:")
traverse_list(list_1)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Update an element in a list                                                                                                               # Time - Space
#
# Solution:                                                                                                                                 # O(1) - O(1)
def update_element_list(list, index, value):
    if index >= len(list):
        return "\tOut of range of list"
    else:
        list[index] = value
        return list


print(
    "DS - Update an element in a list - Solution: \n\t{}".format(
        update_element_list(list_2, 1, 9)
    )
)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Insert an element in a list                                                                                                               # Time - Space
#
# Solution 1:                                                                                                                               # O(n) - O(1)
list_insert_1 = list_3
list_insert_1.insert(2, 9)
print("DS - Insert an element in a list - Solution 1: \n\t{}".format(list_insert_1))
# Solution 2:                                                                                                                               # O(1) - O(1)
list_insert_2 = list_3
list_insert_2.append(8)
print("DS - Insert an element in a list - Solution 2: \n\t{}".format(list_insert_2))
# Solution 3:                                                                                                                               # O(n) - O(1)
list_insert_3 = list_3
list_insert_3.extend(list_2)
print("DS - Insert an element in a list - Solution 3: \n\t{}".format(list_insert_3))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Delete elements in a list                                                                                                                 # Time - Space
#
# Solution 1:                                                                                                                               # O(1) - O(1)
list_insert_3.pop(1)
print("DS - Delete elements in a list - Solution 1: \n\t{}".format(list_insert_3))
# Solution 2:                                                                                                                               # O(1) - O(1)
list_insert_3.remove(3)
print("DS - Delete elements in a list - Solution 2: \n\t{}".format(list_insert_3))
# Solution 3:                                                                                                                               # O(1) - O(1)
del list_insert_3[:2]
print("DS - Delete elements in a list - Solution 3: \n\t{}".format(list_insert_3))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Search an element in a list                                                                                                               # Time - Space
#
# Solution 1: Using operator                                                                                                                # O(n) - O(1)
def search_element_list_1(list, value):
    if value in list:
        print(f"\t{value} is in the list")
    else:
        print(f"\t{value} is not in the list")


print("DS - Search an element in a list - Solution 1:")
search_element_list_1(list_insert_2, 3)


# Solution 2: Linear search                                                                                                                 # O(n) - O(1)
def search_element_list_2(list, value):
    for index, element in enumerate(list):
        if element == value:
            return "\n\tFound value at index {}".format(index)
    return f"{value} is not found"


print(
    "DS - Search an element in a list - Solution 2: {}".format(
        search_element_list_2(list_insert_2, 8)
    )
)
