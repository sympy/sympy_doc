n = 6
b = Beam(10*n, E, I)
for i in range(n):
    b.apply_load(1 / (5**i), 10*i + 5, i, end=10*i + 10)
plot(b.load, (x, 0, 10*n))  # doctest: +SKIP
