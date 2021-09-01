from sympy.physics.continuum_mechanics.beam import Beam3D
from sympy import symbols
l, E, G, I, A, x = symbols('l, E, G, I, A, x')
b = Beam3D(20, E, G, I, A, x)
subs = {E:40, G:21, I:100, A:25}
b.apply_load(15, start=0, order=0, dir="z")
b.apply_load(12*x, start=0, order=0, dir="y")
b.bc_deflection = [(0, [0, 0, 0]), (20, [0, 0, 0])]
R1, R2, R3, R4 = symbols('R1, R2, R3, R4')
b.apply_load(R1, start=0, order=-1, dir="z")
b.apply_load(R2, start=20, order=-1, dir="z")
b.apply_load(R3, start=0, order=-1, dir="y")
b.apply_load(R4, start=20, order=-1, dir="y")
b.solve_for_reaction_loads(R1, R2, R3, R4)
b.solve_slope_deflection()
b.plot_loading_results('y',subs)
# PlotGrid object containing:
# Plot[0]:Plot object containing:
# [0]: cartesian line: -6*x**2 for x over (0.0, 20.0)
# Plot[1]:Plot object containing:
# [0]: cartesian line: -15*x**2/2 for x over (0.0, 20.0)
# Plot[2]:Plot object containing:
# [0]: cartesian line: -x**3/1600 + 3*x**2/160 - x/8 for x over (0.0, 20.0)
# Plot[3]:Plot object containing:
# [0]: cartesian line: x**5/40000 - 4013*x**3/90300 + 26*x**2/43 + 1520*x/903 for x over (0.0, 20.0)
