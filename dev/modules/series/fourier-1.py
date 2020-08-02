from sympy import fourier_series, pi, plot
from sympy.abc import x
f = x
s = fourier_series(f, (x, -pi, pi))
s1 = s.truncate(n = 3)
s2 = s.truncate(n = 5)
s3 = s.truncate(n = 7)
p = plot(f, s1, s2, s3, (x, -pi, pi), show=False, legend=True)

p[0].line_color = (0, 0, 0)
p[0].label = 'x'
p[1].line_color = (0.7, 0.7, 0.7)
p[1].label = 'n=3'
p[2].line_color = (0.5, 0.5, 0.5)
p[2].label = 'n=5'
p[3].line_color = (0.3, 0.3, 0.3)
p[3].label = 'n=7'

p.show()
