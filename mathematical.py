from sympy import (
    diff, integrate, sin, cos, 
    exp, limit, solve, oo
)
from sympy.abc import x
if __name__ == "__main__":
    print("The derivative of sin(x)*e^x is :", diff(sin(x)*exp(x), x))
    print(
        "The indefinite integration of e^x*sin(x)+e^x*cos(x) is :",
        integrate(exp(x)*sin(x) + exp(x)*cos(x), x)
    )
    print(
        "The definite integration of sin(x^2) from -oo to oo is :",
        integrate(sin(x**2), (x, -oo, oo))
    )
    print(
        "The limit of sin(x)/x as x tends to 0 is :",
        limit(sin(x)/x, x, 0)
    )
    print(
        "The roots of the equation x^2-2 = 0 are :",
        solve(x**2 - 2, x)
    )