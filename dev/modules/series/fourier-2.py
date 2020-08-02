s1 = fourier_series(x, (x, -1, 1)).truncate(10)
s2 = fourier_series(x, (x, -pi, pi)).truncate(10)
s3 = fourier_series(x, (x, 0, 1)).truncate(10)
p = plot(x, s1, s2, s3, (x, -5, 5), show=False, legend=True)

p[0].line_color = (0, 0, 0)
p[0].label = 'x'
p[1].line_color = (0.7, 0.7, 0.7)
p[1].label = '[-1, 1]'
p[2].line_color = (0.5, 0.5, 0.5)
p[2].label = '[-pi, pi]'
p[3].line_color = (0.3, 0.3, 0.3)
p[3].label = '[0, 1]'

p.show()
