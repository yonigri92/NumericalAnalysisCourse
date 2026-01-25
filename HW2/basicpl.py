from numpy.polynomial import Polynomial

def basic_polinom(roots): # gets roots of polinom creates basic polinom
    basic_pol = []
    num = Polynomial([1.0])
    basic_pol.append(num)

    for i in range(len(roots) - 1):
        # polynomail creates polinot with given variables
        # so given [-roots[i], 1.0] we get  -roots[i] +  1.0*X =>  (x - xi)
        # theres a - because in the interpulation we need X to go to zero in the roots and
        # we keep multiplying be the previus polynom simply because that's how you build simple polynom
        # as in (x - x0)(x - x1)(x - x2)
        num = num * Polynomial([-roots[i], 1.0])
        basic_pol.append(num)
    return basic_pol
