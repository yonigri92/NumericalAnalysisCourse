import numpy as np
def multiply_matrix_vector(matrix, vector):
    """
        Multiplies a matrix by a vector.
        :param matrix: The matrix (list of lists)
        :param vector: The vector (list)
        :return: list - The result vector
        """
    """
    result = Matrix * Vector
    """
    n = len(vector)
    result = []
    for i in range(n):
        val = 0
        for j in range(n):
            val += matrix[i][j] * vector[j]
        result.append(val)
    return result


def simplecalculatematrix(matrixA, SizeN, Vectorb):
    """
        :param matrixA: The coefficient matrix
        :param SizeN: The size of the matrix
        :param Vectorb: The result vector
        :return: list - The solution vector x
        """
    """
    Calculation: x = A^(-1) * b
    Method:
    1. Calculate A^(-1) using NumPy
    2. Multiply A^(-1) * b.
    """
    try:
        a_arr = np.array(matrixA)
        np_inverse = np.linalg.inv(a_arr)
        inverse = np_inverse.tolist()
        result_x = multiply_matrix_vector(inverse, Vectorb)
        return result_x
    except np.linalg.LinAlgError:
        print("Error: doesnt have single solution.")
        return None