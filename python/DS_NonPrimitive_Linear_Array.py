# **********************************************************************************************************************************************************************
# DATA STRUCTURE - ARRAY
# **********************************************************************************************************************************************************************
# Create an Array                                                                                                                   # Time - Space
#
# Solution 1: Using array library                                                                                                   # O(1) - O(1) / O(n) - O(n)
import array
array_array_library_1 = array.array('i')                                                                                            # O(1) - O(1)
array_array_library_2 = array.array('i',[1,2,3])                                                                                    # O(n) - O(n)
print("Create an array - Solution 1: \n\t{} \n\t{}"
      .format(array_array_library_1, array_array_library_2))

# Solution 2: Using numpy library                                                                                                   # O(1) - O(1) / O(n) - O(n)
import numpy
array_numpy_library_1 = numpy.array([], dtype=int)                                                                                  # O(1) - O(1)
array_numpy_library_2 = numpy.array([1,2,3])                                                                                        # O(n) - O(n)
print("Create an array - Solution 2: \n\t{} \n\t{}"
      .format(array_numpy_library_1,array_numpy_library_2))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Insert an element to an array                                                                                                     # Time - Space
#
# Solution                                                                                                                          # O(n) - O(1)
array_array_library_1.insert(0,6)                                                                                                   # O(n) - O(1)
array_array_library_2.insert(0,6)                                                                                                   # O(n) - O(1)
array_numpy_library_1 = numpy.insert(array_numpy_library_1,0,6)                                                                     # O(n) - O(1)
array_numpy_library_2 = numpy.insert(array_numpy_library_2,0,6)                                                                     # O(n) - O(1)
print("Insert elements to an array - Solution: \n\t{}\n\t{}\n\t{}\n\t{}"
      .format(array_array_library_1,array_array_library_2,array_numpy_library_1,array_numpy_library_2))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Traverse an array                                                                                                                 # Time - Space
#
# Solution                                                                                                                          # O(n) - O(1)
def traverse_array(array):                                                                                                          # O(n) - O(1)
    for element in array:                                                                                                           # O(n) - O(1)
        print("\t{}".format(element))                                                                                               # O(1) - O(1)
print("Traverse an array - Solution:")
traverse_array(array_numpy_library_2)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Access an element in an array                                                                                                     # Time - Space
#
# Solution                                                                                                                          # O(1) - O(1)
def access_element_array(array, index):                                                                                             # O(1) - O(1)
    if index >= len(array):                                                                                                         # O(1) - O(1)
        print("There is no element in array")                                                                                       # O(1) - O(1)
    else:                                                                                                                           # O(1) - O(1)
        print("\t{}".format(array[index]))                                                                                          # O(1) - O(1)
print("Access an element in an array - Solution:")
access_element_array(array_numpy_library_2,3)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Update an element in an array                                                                                                     # Time - Space
#
# Solution                                                                                                                          # O(1) - O(1)
def update_element_array(array,index,value):                                                                                        # O(1) - O(1)
    if index >= len(array):                                                                                                         # O(1) - O(1)
        print("There is no element in array")                                                                                       # O(1) - O(1)
    else:                                                                                                                           # O(1) - O(1)
        array[index] = value                                                                                                        # O(1) - O(1)
print("Update an element in an array - Solution:")
update_element_array(array_numpy_library_2,0,9)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Search an element in an array                                                                                                     # Time - Space
#
# Solution                                                                                                                          # O(n) - O(1)
def search_element_array(array,value):                                                                                              # O(n) - O(1)
    for index in range(len(array)):                                                                                                 # O(n) - O(1)
        if array[index] == value:                                                                                                   # O(1) - O(1)
            print("\tDetect element {} in array at index {}".format(array[index],index-1))                                          # O(1) - O(1)
        else:                                                                                                                       # O(1) - O(1)
            pass                                                                                                                    # O(1) - O(1)
print("Search an element in an array - Solution:")
search_element_array(array_numpy_library_2,3)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Delete an element in an array                                                                                                     # Time - Space
#
# Solution 1: Using array library                                                                                                   # O(n) - O(1)
array_element_arraylib_delete = array_array_library_2                                                                               # O(1) - O(1)
array_element_arraylib_delete.remove(1)                                                                                             # O(n) - O(1)
print("Delete an element in an array - Solution 1: \n\t{}".format(array_element_arraylib_delete))
# Solution 2: Using numpy library
array_element_numpylib_delete = numpy.delete(array_numpy_library_2,1)                                                               # O(n) - O(1)
print("Delete an element in an array - Solution 2: \n\t{}".format(array_element_numpylib_delete))


