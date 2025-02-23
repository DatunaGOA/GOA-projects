import math

def find_next_square(sq):
    if math.isqrt(sq) ** 2 == sq:
        next_num = math.isqrt(sq) + 1
        return next_num ** 2
    else:
        return -1
