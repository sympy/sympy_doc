from sympy import symbols
from sympy.plotting import plot, plot3d, PlotGrid
x, y = symbols('x, y')
p1 = plot(x, x**2, x**3, (x, -5, 5))
p2 = plot((x**2, (x, -6, 6)), (x, (x, -5, 5)))
p3 = plot(x**3, (x, -5, 5))
p4 = plot3d(x*y, (x, -5, 5), (y, -5, 5))
