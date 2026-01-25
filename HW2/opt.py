from numpy.polynomial import Polynomial
import numpy as np
from basicpl import basic_polinom

def opt_distance_interpulation(f,a,b,n):
        k = np.arange(n + 1)
        x = np.cos((2 * k + 1) * np.pi / (2 * (n + 1)))
        cheby =  0.5 * (a + b) + 0.5 * (b - a) * x
        bpolinom = basic_polinom(cheby)
        y = f(cheby)
        coef = np.copy(y)
        for j in range(1, n + 1):
            for i in range(n, j - 1, -1):
                coef[i] = (coef[i] - coef[i - 1]) / (cheby[i] - cheby[i - j])
        p = Polynomial([0.0])
        for i in range(len(coef)):
            p = p + coef[i] * bpolinom[i]
        return p
