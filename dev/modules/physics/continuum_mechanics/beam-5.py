from sympy import symbols
from sympy.physics.continuum_mechanics.beam import Beam
E, I = symbols('E, I')
R_0, R_8 = symbols('R_0, R_8')
b = Beam(12, E, I)
b.apply_support(0, 'roller')
b.apply_support(8, 'roller')
b.solve_for_ild_reactions(1, R_0, R_8)
b.solve_for_ild_shear(4, 1, R_0, R_8)
b.ild_shear
# Piecewise((x/8, x < 4), (x/8 - 1, x > 4))
b.plot_ild_shear()
# Plot object containing:
# [0]: cartesian line: Piecewise((x/8, x < 4), (x/8 - 1, x > 4)) for x over (0.0, 12.0)
