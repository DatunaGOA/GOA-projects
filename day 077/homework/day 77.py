# davaleba 1
def print_positions(rows, cols):
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            print(f"row: {row} col: {col}")

# davaleba 2
def multiplication_table():
    return [[(i + 1) * (j + 1) for j in range(10)] for i in range(10)]

# davaleba 3
def print_increasing_pairs(n):
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            print(f"({i}, {j})")
