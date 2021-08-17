from sympy.abc import s
from sympy.physics.control.lti import TransferFunction
from sympy.physics.control.control_plots import ramp_response_plot
tf1 = TransferFunction(s, (s+4)*(s+8), s)
ramp_response_plot(tf1, upper_limit=2)   # doctest: +SKIP
