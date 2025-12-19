import numpy as np


def is_singlesolution(A):
    """"5.2"""
    det = np.linalg.det(A)
    return not np.isclose(det, 0)

def get_bjmax(A):
    """5.3 Bj = D^-1 * (L + U)"""
    Bj = np.linalg.inv(np.diag(np.diag(A))) @ (A - np.diag(np.diag(A)))
    value = np.linalg.eigvals(Bj)
    bjmax = max(abs(value))
    return bjmax


def yakobi(A, b, x0, eps):
    """5.3 """
    inverted = np.linalg.inv(np.diag(np.diag(A)))
    LplusU = A - np.diag(np.diag(A))

    starting_vector = np.array(x0).astype(float)
    i = 0
    for i in range (1000):
        """m_plus_one_vector = X^m+1
           what we do:
           x^(m+1) = D^-1 * (b - (LU)x^m)
           and we keep on doing it inside the for either 1000 times 
           or until  max{abs(m_plus_one_vector - starting_vector)}< eps
        """
        m_plus_one_vector = inverted @ (b - LplusU @ starting_vector)
        diff = m_plus_one_vector - starting_vector
        abs_diff = np.abs(diff)
        max_diff = np.max(abs_diff)
        if max_diff < eps:
            return m_plus_one_vector, i+1
        else:
            starting_vector = m_plus_one_vector
    return starting_vector, i

""" 5.1"""
def yaakobi_algorithem(A, b, x0, eps):
    """ 5.2"""
    if not is_singlesolution(A):
        print("no single solution use different method")
        return
    print("there is a single solution ")
    """ 5.3"""
    bjmax = get_bjmax(A)
    print("sufficient and must condition is met ")
    if not bjmax < 1:
        print(f"yaakobi dont mitcanes bjmax: {bjmax:.4f} > 1")
        print("use a different solution")
    else:
        solution, i = yakobi(A, b, x0, eps)
        print(f"sol: {solution}")
        print(f" i = {i}")

if __name__ == "__main__":

    print("Exersice A:")
    yaakobi_algorithem(np.array([[1, 2],[2, 4]]), np.array([5, 10]), [0] * 2,  0.001)
    print("Exersice B:")
    yaakobi_algorithem(np.array([[10, 2, 1],[1, 5, 1],[2, 3, 10]]), np.array([7, -8, 6]), [0] * 3, 10 ** -5)
    print("Exersice C:")
    yaakobi_algorithem(np.array([[1, 4],[3, 1]]), np.array([5, 4]), [0] * 2,  0.001)
    print("Exersice D:")
    yaakobi_algorithem(np.array([[1, 1, 0, 0], [-1, 0, 1, 0], [0, -1, 0, 1], [0, 0, -1, -1]]), np.array([100, -50, -50, 0 ]), [0] * 4, 0.001)