from sympy.physics.continuum_mechanics.beam import Beam3D
from sympy import symbols
l, E, G, I, A, x = symbols('l, E, G, I, A, x')
b = Beam3D(20, 40, 21, 100, 25, x)
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
b.max_deflection()
# [(0, 0), (10, 495/14), (-10 + 10*sqrt(10793)/43, (10 - 10*sqrt(10793)/43)**3/160 - 20/7 + (10 - 10*sqrt(10793)/43)**4/6400 + 20*sqrt(10793)/301 + 27*(10 - 10*sqrt(10793)/43)**2/560)]
