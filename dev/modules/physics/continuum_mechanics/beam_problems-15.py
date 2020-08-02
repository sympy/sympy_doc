from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols, plot, S
E, I = symbols('E, I')
R1, R2 = symbols('R1, R2')
b = Beam(6, E, I)
b.apply_load(R1, 0, -1)
b.apply_load(-S(3)/2, 3, -2)
b.apply_load(3, 3, 0)
b.apply_load(1, 3, 1)
b.apply_load(R2, 6, -1)
b.bc_deflection.append((0, 0))
b.bc_deflection.append((6, 0))
b.solve_for_reaction_loads(R1, R2)
b.reaction_loads
# {R₁: -11/4, R₂: -43/4}

b.load
# -1            -2                                     -1
# 11⋅<x>     3⋅<x - 3>              0          1   43⋅<x - 6>
# - ──────── - ─────────── + 3⋅<x - 3>  + <x - 3>  - ────────────
# 4            2                                     4
