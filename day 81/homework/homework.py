# 1) 
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 2) 
def count_odd_digits(num):
    return sum(1 for digit in str(abs(num)) if int(digit) % 2 != 0)

# 3) 
def filter_numbers(numbers):
    return [num for num in numbers if 
            (num < 100 and ((num % 3 == 0 and num % 6 != 0) or 
                            (num % 5 == 0 and num % 10 != 0)))]

# 4) 
def count_left_symbols(symbols):
    return [symbols[:i].count(symbols[i]) for i in range(len(symbols))]
