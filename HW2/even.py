from numpy.polynomial import Polynomial
import numpy as np
from basicpl import basic_polinom


def even_distance_interpulation(f,a,b,n):
    equal_distx = np.linspace(a, b, n + 1) # equal distance locations
    bpolinom = basic_polinom(equal_distx)
    y = f(equal_distx)
    coef = np.copy(y)
    for j in range(1, n+1):
        for i in range(n, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (equal_distx[i] - equal_distx[i - j])
    p = Polynomial([0.0])
    for i in range(len(coef)):
        p = p + coef[i] * bpolinom[i]
    return p