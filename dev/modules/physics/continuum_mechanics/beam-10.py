from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
R1, R2 = symbols('R1, R2')
b = Beam(8, 200*(10**9), 400*(10**-6))
b.apply_load(5000, 2, -1)
b.apply_load(R1, 0, -1)
b.apply_load(R2, 8, -1)
b.apply_load(10000, 4, 0, end=8)
b.bc_deflection = [(0, 0), (8, 0)]
b.solve_for_reaction_loads(R1, R2)
b.plot_slope()
# Plot object containing:
# [0]: cartesian line: -8.59375e-5*SingularityFunction(x, 0, 2) + 3.125e-5*SingularityFunction(x, 2, 2)
# + 2.08333333333333e-5*SingularityFunction(x, 4, 3) - 0.0001953125*SingularityFunction(x, 8, 2)
# - 2.08333333333333e-5*SingularityFunction(x, 8, 3) + 0.00138541666666667 for x over (0.0, 8.0)
