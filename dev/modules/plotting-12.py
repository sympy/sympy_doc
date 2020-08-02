from sympy import pi
expr1 = (u, cos(2*pi*u)/2 + 1/2)
expr2 = (u, sin(2*pi*u)/2 + 1/2)
p = plot_parametric(expr1, expr2, (u, 0, 1), line_color='blue')
