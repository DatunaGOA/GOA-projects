#1

def likes(names):
    num_likes = len(names)
    if num_likes == 0:
        return "no one likes this"
    elif num_likes == 1:
        return f"{names[0]} likes this"
    elif num_likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {num_likes - 2} others like this"

print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))


#2

def sum_of_multiples(n):
    if n < 0:
        return 0
    
    multiples_sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            multiples_sum += i
    
    return multiples_sum

print(sum_of_multiples(10))
