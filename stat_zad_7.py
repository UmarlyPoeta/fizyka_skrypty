import sympy as sp

x = sp.symbols('x')

A = sp.Matrix([[7,7,7],
               [7,7,7],
               [7,7,7]])

char_poly = (A - x * sp.eye(3)).det()
solutions = sp.solve(char_poly, x)

print(solutions)