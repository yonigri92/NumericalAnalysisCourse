import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from even import even_distance_interpulation
from opt import opt_distance_interpulation

x_start = 0
x_end = 1
def f(x):
    return 1 / (x + 1)
if __name__ == '__main__':

    a, b = x_start, x_end
    for n in [2,4,6,8]:
        even = even_distance_interpulation(f, a, b, n)
        opt = opt_distance_interpulation(f, a, b, n)
        print( "Even Distance Ln(E;x):")
        print(even)
        print("Optimal Distance Ln(T;x):")
        print(opt)
        x_axis = np.linspace(a, b, 400)
        y_t = f(x_axis)
        y_e = even(x_axis)
        y_o = opt(x_axis)
        plt.figure(figsize=(15, 10))
        plt.title(f'n = {n}')
        plt.plot(x_axis, y_t, 'k-', linewidth=2, label='F(X): ')
        plt.plot(x_axis, y_o, 'g-', label=f'Ln(T;x): ')
        plt.plot(x_axis, y_e, 'r--', label=f'Ln(E;x): ')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.ylim(0, 1.5)
        plt.legend()
        plt.grid(True)

        plt.show()