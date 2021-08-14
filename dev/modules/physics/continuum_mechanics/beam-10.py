from sympy import symbols
from sympy.physics.continuum_mechanics.beam import Beam
E, I = symbols('E, I')
R_0, R_8 = symbols('R_0, R_8')
b = Beam(12, E, I)
b.apply_support(0, 'roller')
b.apply_support(8, 'roller')
b.solve_for_ild_reactions(1, R_0, R_8)
b.solve_for_ild_moment(4, 1, R_0, R_8)
b.ild_moment
# Piecewise((-x/2, x < 4), (x/2 - 4, x > 4))
