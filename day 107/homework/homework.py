
#1
def sum_two_largest(numbers):
    largest, second_largest = sorted(numbers)[-2:]  
    return largest + second_largest








#2
def last_repeated_element(numbers):
    seen = set()
    last_repeated = None
    for num in reversed(numbers):  
        if num in seen:
            last_repeated = num
            break
        seen.add(num)
    return last_repeated if last_repeated is not None else "მასივში არცერთი ელემენტი არ მეორდება"









#3
def count_larger_left(numbers):
    result = [sum(1 for x in numbers[:i] if x < numbers[i]) for i in range(len(numbers))]
    return result











n = int(input("Enter n: ")) 
numbers = list(map(int, input(f"Enter {n} numbers: ").split()))
print("1) ორი უდიდესი ელემენტის ჯამი:", sum_two_largest(numbers))
print("2) ბოლოს გამეორებული ელემენტი:", last_repeated_element(numbers))
print("3) მარცხნივ მყოფზე მეტების რაოდენობა:", count_larger_left(numbers))
