def square_digits(num):
    num_str = str(num)
    res = ""
    for digit in num_str:
        res += str(int(digit) ** 2)
    return int(res)