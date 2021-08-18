from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
R1, R2 = symbols('R1, R2')
b = Beam(8, 200*(10**9), 400*(10**-6), 2)
b.apply_load(5000, 2, -1)
b.apply_load(R1, 0, -1)
b.apply_load(R2, 8, -1)
b.apply_load(10000, 4, 0, end=8)
b.bc_deflection = [(0, 0), (8, 0)]
b.solve_for_reaction_loads(R1, R2)
b.plot_shear_stress()
# Plot object containing:
# [0]: cartesian line: 6875*SingularityFunction(x, 0, 0) - 2500*SingularityFunction(x, 2, 0)
# - 5000*SingularityFunction(x, 4, 1) + 15625*SingularityFunction(x, 8, 0)
# + 5000*SingularityFunction(x, 8, 1) for x over (0.0, 8.0)
