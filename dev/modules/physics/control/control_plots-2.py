from sympy.abc import s
from sympy.physics.control.lti import TransferFunction
from sympy.physics.control.control_plots import bode_plot
tf1 = TransferFunction(1*s**2 + 0.1*s + 7.5, 1*s**4 + 0.12*s**3 + 9*s**2, s)
bode_plot(tf1, initial_exp=0.2, final_exp=0.7)   # doctest: +SKIP
