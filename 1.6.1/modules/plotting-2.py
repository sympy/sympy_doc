from sympy import symbols
from sympy.plotting import plot
x = symbols('x')
p1 = plot(x**2, show=False)
p2 = plot(x, -x, show=False)
p1.extend(p2)
p1
# Plot object containing:
# [0]: cartesian line: x**2 for x over (-10.0, 10.0)
# [1]: cartesian line: x for x over (-10.0, 10.0)
# [2]: cartesian line: -x for x over (-10.0, 10.0)
p1.show()
