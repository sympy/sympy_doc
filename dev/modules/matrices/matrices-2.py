A = Matrix([[1, -1], [-1, 1]])
A.is_positive_definite
# False
A.is_positive_semidefinite
# True

p = plot3d((x.T*A*x)[0, 0], (a, -1, 1), (b, -1, 1))
