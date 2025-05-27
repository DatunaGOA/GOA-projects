#1
def sum_digits(n):
    n = abs(n)
    total = 0
    for digit in str(n):
        total += int(digit)
    return total










#2
def sum_two_largest(lst):
    unique_numbers = sorted(set(lst), reverse=True)
    return unique_numbers[0] + unique_numbers[1] if len(unique_numbers) > 1 else unique_numbers[0]













#testing cases lol
print(sum_digits(123)) 
print(sum_digits(-405))  
print(sum_two_largest([3, 7, 2, 9, 5]))  
print(sum_two_largest([10, 10, 5, 3]))  
