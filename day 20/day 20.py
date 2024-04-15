def arithmetic(num):
    if not num:
        return 0 
    return sum(num) / len(num)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean = arithmetic(list)
print("Arithmetic mean:", mean)


def filter_num(num):
    pos_numbers = [num for num in num if num > 0]
    neg_numbers = [num for num in num if num < 0]
    return pos_numbers, neg_numbers

# Example usage:
my_list = [1, -2, -3, 4, 5, -6, -12, 3]
positive, negative = filter_num(my_list)
print("Positive numbers:", positive)
print("Negative numbers:", negative)