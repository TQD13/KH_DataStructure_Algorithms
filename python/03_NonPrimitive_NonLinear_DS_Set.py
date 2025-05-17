# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SET - OPERATOR
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
set_op = {1, 2, 3}
print(f"Operator = - Assignment: {set_op}")
print(f"Operator == != etc. - Check 2 sets with Venn Diagram: {set_op != {8,9}}")
print(f"Operator | - Union: {set_op | {4,5,6,7}}")
print(f"Operator & - Intersection: {set_op & {8,9}}")
print(f"Operator - - Difference: {set_op - {8,9}}")
print(f"Operator ^ - Symmetric difference: {set_op ^ {0,1}}")
set_op |= {4, 5, 6, 7}
print(f"Operator |= &= -= ^= - Update assignment: {set_op}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SET - METHOD
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
set_1 = {1, 2, 3}
set_1.add(4)
print(f"Method add(...) - Add an item to set: {set_1}")
set_2 = {"a", "b"}
set_2.clear()
print(f"Mehtod clear() - Remove all items from a set: {set_2}")
set_3 = set_1.copy()
print(f"Method copy() - Return a shallow copy of the set: {set_3}")
print(f"Method difference(...) - Return difference set: {set_1.difference({5,6})}")
set_3.difference_update({2, 4})
print(
    f"Method difference_update(...) - Remove found item in others and update set: {set_3}"
)
set_3.discard(2)
print(f"Method discard(...) - Remove an item in set: {set_3}")
print(
    f"Method intersection(...) - Return an intersection set: {set_1.intersection({3,4})}"
)
set_op.intersection_update({-1, 0, 1, 2, 3, 4, 5})
print(
    f"Method intersection_update(...) - Remove difference items and update set: {set_op}"
)
print(
    f"Method isdisjoint(...) - Return whether 2 sets have a intersection or not: {set_3.isdisjoint({1})}"
)
print(
    f"Method issubset(...) - Return whether another set contains this set or not: {set_3.issubset({1,2,3,4,5})}"
)
print(
    f"Method issupperset(...) - Return whether this set contains another set or not: {set_3.issuperset({1})}"
)
set_3.pop()
print(f"Method pop() - Remove a random item in set: {set_3}")
set_1.remove(1)
print(f"Method remove(...) - Remove a item in set: {set_1}")
print(
    f"Method symmetric_difference(...) - Return a symmetric difference set: {set_3.symmetric_difference({3,4,5})}"
)
print(
    f"Method symmetric_difference_update(...) - Insert a symmetric differences from this set to another: {set_3.symmetric_difference_update({3,4,5})}"
)
set_3.union({5, 6, 7, 8})
print(f"Method union(...) - Return union set: {set_3}")
set_2.update({"a"})
print(f"Method update(...) - Udpate union set of this set to another: {set_2}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SET - BUILT-IN FUNCTION
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(f"Built-in function len(...) - Return number item in set: {len(set_3)}")
print(f"Built-in function max(...) - Return the maximum item: {max(set_3)}")
print(f"Built-in function min(...) - Return the minimum item: {min(set_3)}")
print(f"Built-in function sum(...) - Return the sum of items: {sum(set_3)}")
print(f"Built-in function sorted(...) - Return the sorted list of set: {sorted(set_3)}")
print(f"Built-in function any(...) - Return True if any item is truthy: {any(set_3)}")
print(f"Built-in function all(...) - Return True if all items are truthy: {all(set_3)}")
print(
    f"Built-in function enumerate(...) - Return enumerate object (index,value): {list(enumerate(set_3))}"
)
print("Built-in function iter(...) - Return an iterator over set:")
for item in iter(set_3):
    print(f"\t{item}")
print(f"Built-in function type(...) - Return the type data: {type(set_3)}")
print(f"Built-in function frozenset(...) - Create an immutable set: {frozenset(set_3)}")
print(f"Built-in function set(...) - Create a set: {set([1,2])}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SET - DATA STRUCTURE
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create a set                                                                                                                                  # Time - Space
#
# Solution 1:                                                                                                                                   # O(n) - O(1)
set_ds_1 = {1, 2, 3, 4, 5}
print(f"DS - Create a set - Solution 1: {set_ds_1}")
# Solution 2: Using set function                                                                                                                # O(n) - O(1)
set_ds_2 = set([1, 2, 3, 4, 5])
print(f"DS - Create a set - Solution 2: {set_ds_2}")
# Solution 3: Set comprehension                                                                                                                 # O(n) - O(1)
set_ds_3 = {item for item in "abcdef" if item not in "abc"}
print(f"DS - Create a set - Solution 3: {set_ds_3}")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Access an item in set                                                                                                                         # Time - Space
#
# Solution:                                                                                                                                     # O(n) - O(1)
def access_item_set(set_ds, value):
    for item in set_ds:
        if item == value:
            return item
    return "None"


print(f"DS - Access an item in set - Solution: {access_item_set(set_ds_1,1)}")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Traverse items in set                                                                                                                         # Time - Space
#
# Solution:                                                                                                                                     # O(n) - O(1)
def traverse_item_set(set_ds):
    for item in set_ds:
        print(f"\t{item}")


print("DS - Traverse items in set - Solution:")
traverse_item_set(set_ds_3)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Search an item in set                                                                                                                         # Time - Space
#
# Solution:                                                                                                                                     # O(n) - O(1)
print(f"DS - Search an item in set - Solution: {3 in set_ds_3}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Insert an item in set                                                                                                                          # Time - Space
#
# Solution:                                                                                                                                      # O(n) - O(1)
set_ds_3.add("h")
print(f"DS - Insert an item in set - Solution: {set_ds_3}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Delete items in set                                                                                                                            # Time - Space
#
# Solution:                                                                                                                                      # O(n) - O(1)
set_ds_3.clear()
print(f"DS - Delete items in set - Solution: {set_ds_3}")
