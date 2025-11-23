import GetPartialSol

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def main(matrixA, SizeN,Vectorb):
    if(isSingleSol(matrixA)):
        SimpleAnswer = SimpleCalculateMatrix(matrixA,SizeN,Vectorb)
        PartialSol = GetPartialSol(matrixA,SizeN,Vectorb)
        print(PrintClosnesVector(SimpleAnswer,PartialSol))
def isSingleSol(matrixA):
    """
    checks if the matrix has single solution
    """
    value = False
    determinta = get_determinant(matrixA)
    print(f"Calculated Determinant: {determinta}")
    # if det is not zero with small margin return true
    if abs(determinta) > 1e-10:
        return True
    return False
# will return the minor basicly a smaller matrix without  0 line  and j column
def get_minor(matrix, j):
    return [row[:j] + row[j+1:] for row in (matrix[:0] + matrix[0+1:])]


def get_determinant(matrixA):
    """
    calculate the determinant in a recursive way
    """
    SizeN = len(matrixA)
    # if matrix is sizeN == 1 then matrix size is 1 on 1
    if SizeN == 1:
        return matrixA[0][0]
    det = 0
    # go over all the first row
    for i in range(SizeN):
         # change the mark so that even times will be + and uneven -
        sign = (-1) ** i
        current = matrixA[0][i]
         #get the minor
        inner_matrix = get_minor(matrixA, i)
        inner_det = get_determinant(inner_matrix)
        det += sign * current * inner_det

    return det


def SimpleCalculateMatrix(matrixA, SizeN, Vectorb):
    """
     just simple gaos solution
     get upper traingle and then calculate with the solution we get
    """

    # copy matrix and vector
    matrix = [list(map(float, row)) for row in matrixA]
    vector = list(map(float, Vectorb))

    x = [0] * SizeN  # solution will be here

    # forward part - upper triangle
    for i in range(SizeN):

        # if the pivot is 0 we need to change the line so we can continue
        if abs(matrix[i][i]) == 0:
            found_swap = False
            for k in range(i + 1, SizeN):
                #find pyvot that isnt zero and exchange between the lines
                if abs(matrix[k][i]) != 0:
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    vector[i], vector[k] = vector[k], vector[i]
                    found_swap = True
                    break

        # איפוס כל האיברים מתחת לפיבוט בעמודה הנוכחית
        for k in range(i + 1, SizeN):
            factor = mat[k][i] / mat[i][i]

            # עדכון השורה k במטריצה (Rk = Rk - factor * Ri)
            for j in range(i, SizeN):  # מתחילים מ-i כי לפני זה הכל אפסים
                mat[k][j] -= factor * mat[i][j]

            # עדכון וקטור התוצאות בהתאם
            vec[k] -= factor * vec[i]

    # --- שלב 2: הצבה לאחור (Backward Substitution) ---
    # רצים מהשורה האחרונה (SizeN-1) עד הראשונה (0)
    for i in range(SizeN - 1, -1, -1):
        sum_ax = 0
        # סוכמים את האיברים שכבר מצאנו (מימין לאלכסון)
        for j in range(i + 1, SizeN):
            sum_ax += mat[i][j] * x[j]

        # חילוץ הנעלם הנוכחי
        x[i] = (vec[i] - sum_ax) / mat[i][i]

    return x
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(matrixA,SizeN,Vectorb)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


