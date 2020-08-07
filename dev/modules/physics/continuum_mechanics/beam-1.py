from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
R1, R2 = symbols('R1, R2')
E, I = symbols('E, I')
b = Beam(50, 20, 30)
b.apply_load(10, 2, -1)
b.apply_load(R1, 10, -1)
b.apply_load(R2, 30, -1)
b.apply_load(90, 5, 0, 23)
b.apply_load(10, 30, 1, 50)
b.apply_support(50, "pin")
b.apply_support(0, "fixed")
b.apply_support(20, "roller")
p = b.draw()
p
# Plot object containing:
# [0]: cartesian line: 25*SingularityFunction(x, 5, 0) - 25*SingularityFunction(x, 23, 0)
# + SingularityFunction(x, 30, 1) - 20*SingularityFunction(x, 50, 0)
# - SingularityFunction(x, 50, 1) + 5 for x over (0.0, 50.0)
# [1]: cartesian line: 5 for x over (0.0, 50.0)
p.show()
