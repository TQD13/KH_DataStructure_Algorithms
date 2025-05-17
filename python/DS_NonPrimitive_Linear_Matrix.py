# MATRIX - 2 DIMENTIONAL ARRAY 
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create a matrix                                                                                                                   # Time - Space
#
# Solution: Using numpy library                                                                                                     # O(mn) - O(mn)
import numpy
matrix_numpy_lib = numpy.array([[1,2,3],[4,5,6]])                                                                                   # O(mn) - O(mn)
print("Create a matrix - Solution: {}"
      .format(matrix_numpy_lib))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Insert a row/column into a matrix                                                                                                 # Time - Space
#
# Solution 1: Using numpy append method                                                                                             # O(mn) - O(mn)
matrix_new_1 = numpy.append(matrix_numpy_lib,[[7,8,9]],axis = 0)                                                                    # O(mn) - O(mn)
matrix_new_2 = numpy.append(matrix_numpy_lib,[[0],[0]],axis = 1)                                                                    # O(mn) - O(mn)
print("Insert a row into a matrix - Solution 1: {}".format(matrix_new_1))
print("Insert a column into a matrix - Solution 1: {}".format(matrix_new_2))
# Solution 2: Using numpy insert method                                                                                             # O(mn) - O(mn)
matrix_new_3 = numpy.insert(matrix_numpy_lib,1,[[7,8,9]],axis = 0)                                                                  # O(mn) - O(mn)
matrix_new_4 = numpy.insert(matrix_numpy_lib,0,[[0]],axis = 1)                                                                      # O(mn) - O(mn)
print("Insert a row into a matrix - Solustion 2: {}".format(matrix_new_3))
print("Insert a column into a matrix - Solution 2: {}".format(matrix_new_4))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Traverse a matrix                                                                                                                 # Time - Space
#
# Solution                                                                                                                          # O(mn) - O(1)
def traverse_element_matrix(matrix):                                                                                                # O(mn) - O(1)
    for row in range(len(matrix)):                                                                                                  # O(mn) - O(1)
        for column in range(len(matrix[0])):                                                                                        # O(mn) - O(1)
            print(matrix[row][column])                                                                                              # O(1) - O(1)
print("Traverse a matrix - Solution:")
traverse_element_matrix(matrix_numpy_lib)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Access an element in a matrix                                                                                                     # Time - Space
#
# Solution                                                                                                                          # O(1) - O(1)
def access_element_matrix(matrix,row,column):                                                                                       # O(1) - O(1)
    if row >= len(matrix) or column >= len(matrix[0]):                                                                              # O(1) - O(1)
        print("There is no element in matrix")                                                                                      # O(1) - O(1)
    else:                                                                                                                           # O(1) - O(1)
        print(matrix[row][column])                                                                                                  # O(1) - O(1)
print("Access an element in a matrix - Solution:")
access_element_matrix(matrix_numpy_lib,1,1)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Update an element in a matrix                                                                                                     # Time - Space
#
# Solution                                                                                                                          # O(1) - O(1)
def update_element_matrix(matrix,row,column,value):                                                                                 # O(1) - O(1)
    if row >= len(matrix) or column >= len(matrix[0]):                                                                              # O(1) - O(1)
        return "No element is found"                                                                                                # O(1) - O(1)
    else:                                                                                                                           # O(1) - O(1)
        matrix[row][column] = value                                                                                                 # O(1) - O(1)
        return matrix                                                                                                               # O(1) - O(1)
new_matrix = update_element_matrix(matrix_numpy_lib,1,1,9)
print("Update an element in a matrix - Solution: {}".format(new_matrix))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Search an element in a matrix                                                                                                     # Time - Space
#
# Solution                                                                                                                          # O(mn) - O(1)
def search_element_matrix(matrix, value) -> str:                                                                                    # O(mn) - O(1)
    for row in range(len(matrix)):                                                                                                  # O(mn) - O(1)
        for column in range(len(matrix[0])):                                                                                        # O(n) - O(1)
            if matrix[row][column] == value:                                                                                        # O(1) - O(1)
                return "The value is located at index [" + str(row) + "][" + str(column) + "]"                                      # O(1) - O(1)
    return "The element is not found"                                                                                               # O(1) - O(1)
print("Search an element in a matrix - Solution: {}".format(search_element_matrix(matrix_numpy_lib, 6)))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Delete a row/column in a matrix                                                                                                   # Time - Space
#
# Solution: Using numpy library                                                                                                     # O(mn) - O(mn)
delete_matrix_row = numpy.delete(matrix_new_1, 0, axis = 0)                                                                         # O(mn) - O(mn)
delete_matrix_column = numpy.delete(matrix_new_1,1, axis = 1)                                                                       # O(mn) - O(mn)
print("Delete a row in a matrix - Solution: {}".format(delete_matrix_row))
print("Delete a column in a matrix - Solution: {}".format(delete_matrix_column))


