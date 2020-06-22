A = Matrix([[-1, 0], [0, -1]])
A.is_negative_definite
# True
A.is_negative_semidefinite
# True
A.is_indefinite
# False

p = plot3d((x.T*A*x)[0, 0], (a, -1, 1), (b, -1, 1))
