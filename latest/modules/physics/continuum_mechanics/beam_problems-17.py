b.shear_force()
# 0            -1                       2             0
# 11⋅<x>    3⋅<x - 3>              1   <x - 3>    43⋅<x - 6>
# - ─────── - ─────────── + 3⋅<x - 3>  + ──────── - ───────────
# 4           2                        2            4

b.bending_moment()
# 1            0            2          3             1
# 11⋅<x>    3⋅<x - 3>    3⋅<x - 3>    <x - 3>    43⋅<x - 6>
# - ─────── - ────────── + ────────── + ──────── - ───────────
# 4          2            2           6            4

b.slope()
# 2            1          3          4             2
# 11⋅<x>    3⋅<x - 3>    <x - 3>    <x - 3>    43⋅<x - 6>    78
# - ─────── - ────────── + ──────── + ──────── - ─────────── + ──
# 8          2           2          24           8        5
# ───────────────────────────────────────────────────────────────
# E⋅I


b.deflection()
# 3            2          4          5             3
# 78⋅x   11⋅<x>    3⋅<x - 3>    <x - 3>    <x - 3>    43⋅<x - 6>
# ──── - ─────── - ────────── + ──────── + ──────── - ───────────
# 5        24         4           8         120           24
# ───────────────────────────────────────────────────────────────
# E⋅I
