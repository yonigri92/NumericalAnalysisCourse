from GetPartialSol import GetPartialSol
from simplecalculatematrix import simplecalculatematrix
from helpfuncions import get_determinant
from SimpleCalculateMatrixWithGous import SimpleCalculateMatrixWithGous
def main(matrix_a, size_n, vector_b):
    """

    :param matrix_a is a matrix:
    :param size_n size of the matrix:
    :param vector_b vector B from the formula Ax = b:
    :return void - prints the solution:
    """
    if is_single_sol(matrix_a):
        simple_answer = simplecalculatematrix(matrix_a, size_n, vector_b)
        # since I wrote the function that can calculate using gauss im adding the function
        # here in a comment just remove it if you want to use gauss matrix calculation
        # if you do please add # before simplecalculatematrix so that matrix wont get calculated twice
        #simple_answer = SimpleCalculateMatrixWithGous(matrix_a, size_n, vector_b)
        partial_sol = GetPartialSol(matrix_a, size_n, vector_b)
        print(get_closeness_vector(simple_answer, partial_sol))
    else:
        print('No solution found')
def is_single_sol(matrix_a):
    """
        :param matrix_a: The matrix to check
        :return: boolean - True if determinant is non-zero, False otherwise
        """
    """
    checks if the matrix has single solution
    """
    value = False
    determinate = get_determinant(matrix_a)
    print(f"Calculated Determinant: {determinate}")
    # if det is not zero with small margin return true
    if abs(determinate) > 1e-10:
        return True
    return False
# will return the minor basically a smaller matrix without  0 line  and j column



def get_closeness_vector(simple_answer, partial_sol):
    """
        Calculates the relative error between two solution vectors.
        :param simple_answer: The exact solution vector
        :param partial_sol: The approximate solution vector
        :return: string - The error vector formatted as a string in percentages
        """
    if not simple_answer or not partial_sol:
        return "Error: Empty vector result"

    if len(simple_answer) != len(partial_sol):
        return "Error: Vector size mismatch"

    error_vector = []
    for simpleElement, partialElement in zip(simple_answer, partial_sol):
        if simpleElement == 0:
            error_vector.append(0.0)
        else:
            err = abs((simpleElement - partialElement) / simpleElement) * 100
            error_vector.append(err)

    return f"Error Vector (in %): {error_vector}"


if __name__ == '__main__':
    print("Press 1 to use predetermined input, press 2 to enter your input  ")
    switch = input()
    if switch == '1':
        print("simple solution  ")

        # solve able solution  [1, 1, 1, 1]
        matrix = [
            [4, 1, 1, 1],
            [1, 4, 1, 1],
            [1, 1, 4, 1],
            [1, 1, 1, 4]
        ]
        vector = [7, 7, 7, 7]
        size_n = 4

        print(f"Matrix A: {matrix}")
        print(f"Vector b: {vector}")
        main(matrix, size_n, vector)

        print(" ==========================================================  ")
        print("single solution more complex matrix where we can see the PP algorithem effects")

        matrix2 = [
            [0, 2, 0, 1],
            [2, 2, 3, 2],
            [4, -3, 0, 1],
            [6, 1, -6, -5]
        ]
        vector2 = [0, -2, -7, 6]


        print(f"Matrix A: {matrix2}")
        print(f"Vector b: {vector2}")
        main(matrix2, size_n, vector2)

        print(" ==========================================================  ")
        print("Not single solution")
        # det = 0 second line is double the first one
        matrix2 = [
            [1, 2, 3, 4],
            [2, 4, 6, 8],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        vector2 = [10, 20, 30, 40]

        print(f"Matrix A: {matrix2}")
        print(f"Vector b: {vector2}")
        main(matrix2, size_n, vector2)
    if switch == '2':
        print("Please enter the size of your matrix - only one number as it is squared")
        size_n = input()
        if int(size_n) <= 0:
            print("Error: size of matrix must be > 0")
            exit(1)
        matrix = []
        vector = []
        print("Please enter your matrix ")
        for i in range(int(size_n)):
            row = []
            for j in range(int(size_n)):
                print(f"Enter element row {i}, col {j}:")
                val = float(input())
                row.append(val)
            matrix.append(row)
        print("Please enter your vector ")
        for i in range(int(size_n)):
            val = float(input())
            vector.append(val)
        main(matrix, int(size_n), vector)