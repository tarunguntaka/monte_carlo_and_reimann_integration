import pylab as p


def RI(f, a, b, N):
    """
    This function evaluates the Riemann Integral of a function

    Arguments: float-float function : f
               Lower limit          : a
               Upper limit          : b
               Number of intervals  : N

    f may be pre-defined using the 'lambda' or 'def' methods

    This function works for any f that is defined on [a,b)

    >>> RI(lambda x: x,0,1,1000)
    0.49950000000000017

    >>> RI(lambda x: x,0,1,100.2)
    Traceback (most recent call last):
    ...
    TypeError: N must be a whole number!

    """

    if type(N) == int and N >= 1:
        step = (b - a) / float(N)
        res = 0
        for i in p.linspace(a, b, num=N, endpoint=False):
            res += f(i) * step
        return res
    else:
        raise TypeError('N must be a whole number!')


def seeRiemann(f, a, b, N):
    """
    A little something extra to help visualise the Riemann Integral.
    """
    x = p.arange(a, b, (b - a) / float(N))
    y = f(x)
    p.bar(x, y, width=(b - a) / float(N), linewidth=0)
    p.show()


def MC(f, a, b, n):
    """
    This function evaluates the Monte Carlo approximation
    of an integral

    f may be pre-defined using the 'lambda' or 'def' methods

    This function works for any f that is defined on [a,b)

    Since this method involves taking random function values over an interval,
    results may vary for the same value of 'n'

    """
    import random as r
    Sum = 0
    for i in range(n):
        Sum += f(r.uniform(a, b))
    avg = Sum / float(n)
    return avg * (b - a)


def comp(method, f, a, b):
    """
    This function plots the inverse of the error of the Riemann/Monte Carlo
    Approximation as a function of 'n'.

    'n' ranges from 10 to 1000.

    The argument labelled 'method' takes in only one of two inputs:
        1). RI (Riemann Integral)
        2). MC (Monte Carlo)

    The true value of the integral is evaluated using the 'integrate' method
    which is called from the 'scipy' module.

    """
    from scipy import integrate as i
    accurate = i.quad(f, a, b)[0]
    N = p.linspace(10, 1000, num=990, endpoint=True)
    for n in N:
        error = abs(accurate - method(f, a, b, int(n)))
        p.plot(n, 1.0 / error, 'r.')
    p.show()


"""
The following piece of code plots the RI and MC values as a function of N

Here the function  p.exp(-1*x**2) is being integrated between the limits
0 and 10

N ranges from 10 to 1000

"""


def g(x): return p.exp(-1 * x**2)


n = p.linspace(10, 1000, num=990, endpoint=True)
for i in n:
    p.plot(i, RI(g, 0, 10, int(i)), 'b.')
    p.plot(i, MC(g, 0, 10, int(i)), 'r.')
p.show()


if __name__ == '__main__':
    import doctest as d
    d.testmod()
