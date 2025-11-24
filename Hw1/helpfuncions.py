def get_determinant(matrix_a):
    """
        Creates a minor matrix by removing a specific row and column.
        :param matrix: The original matrix
        :param row_idx: The index of the row to remove
        :param col_idx: The index of the column to remove
        :return: list - The minor matrix
        """
    """
    calculate the determinant in a recursive way
    """
    size_n = len(matrix_a)
    # if matrix is sizeN == 1 then matrix size is 1 on 1
    if size_n == 1:
        return matrix_a[0][0]
    det = 0
    # go over all the first row
    for i in range(size_n):
         # change the mark so that even times will be + and uneven -
        sign = (-1) ** i
        current = matrix_a[0][i]
         #get the minor
        inner_matrix = get_minor(matrix_a, i,0)
        inner_det = get_determinant(inner_matrix)
        det += sign * current * inner_det

    return det

def get_minor(matrix, j,i):
    """
        Calculates the determinant of a matrix recursively.
        :param matrix_a: The matrix to calculate
        :return: float - The determinant value
        """
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

