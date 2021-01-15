R, M = symbols('R, M')
b.apply_load(R, 0, -1)
b.apply_load(M, 0, -2)
b.load
# -2        -1        0             -2            0             -1
# M⋅<x>   + R⋅<x>   + 8⋅<x>  + 50⋅<x - 5>   - 8⋅<x - 5>  + 12⋅<x - 9>
