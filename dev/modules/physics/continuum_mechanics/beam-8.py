from sympy import symbols
from sympy.physics.continuum_mechanics.beam import Beam
E, I = symbols('E, I')
R_0, R_10 = symbols('R_0, R_10')
b = Beam(10, E, I)
b.apply_support(0, 'roller')
b.apply_support(10, 'roller')
b.solve_for_ild_reactions(1,R_0,R_10)
b.ild_reactions
# {R_0: x/10 - 1, R_10: -x/10}
