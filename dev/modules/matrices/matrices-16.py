from sympy import Matrix, symbols
from sympy.plotting import plot3d
a, b = symbols('a b')
x = Matrix([a, b])

A = Matrix([[1, 0], [0, 1]])
A.is_positive_definite
# True
A.is_positive_semidefinite
# True

p = plot3d((x.T*A*x)[0, 0], (a, -1, 1), (b, -1, 1))
