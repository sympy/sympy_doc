from sympy import symbols
from sympy.physics.continuum_mechanics.beam import Beam
E, I = symbols('E, I')
R_0, R_7 = symbols('R_0, R_7')
b = Beam(10, E, I)
b.apply_support(0, 'roller')
b.apply_support(7, 'roller')
b.apply_load(5,4,-1)
b.solve_for_ild_reactions(1,R_0,R_7)
b.ild_reactions
# {R_0: x/7 - 22/7, R_7: -x/7 - 20/7}
b.plot_ild_reactions()
# PlotGrid object containing:
# Plot[0]:Plot object containing:
# [0]: cartesian line: x/7 - 22/7 for x over (0.0, 10.0)
# Plot[1]:Plot object containing:
# [0]: cartesian line: -x/7 - 20/7 for x over (0.0, 10.0)
