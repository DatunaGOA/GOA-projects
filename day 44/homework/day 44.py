
print("Hello, World!")

user_input = input("Enter something: ")
print("You entered:", user_input)


# Single-line comment
"""
Multi-line comment
გოა ბესტ.
"""
print("Comments are used to annotate code for better understanding.")


def example_function():
    for i in range(3):
        print("Inside loop")
    print("Outside loop")

example_function()


long_string = "გოა "\
              "ონ "\
              "ტოპ."
print(long_string)




a = 5  # (ა)ს ველიუ არის 5 'a'
b = 10  # (ბ)ს ველიუ კი 10'b'
c = a + b  # აქ კიდე ცვლადებს ერთმანეთს ვუმატებთ ანუ
("Result:", c)



def sum_numbers(x, y):
    result = x + y
    return result


print("This part is currently disabled.")


x = 10
y = 0

# z = x / y


a = 5  # ინტეგერი
b = 3.14  # ფლოატი
c = "Hello"  #სტრინგი
d = True  # ბულიანი (ბულიონი( უფ უფ რა კაია))


x = 5
y = 10
x, y = y, x
print("შეცვლის შემდეგ: x =", x, "და y =", y)

name = input("Enter your name: ")
age = int(input("Enter your age: "))


global_var = 10

def example_function():
    local_var = 5
    print("Inside function: global_var =", global_var)
    print("Inside function: local_var =", local_var)

example_function()
print("Outside function: global_var =", global_var)


camelCaseVariable = 1
snake_case_variable = 2
CONSTANT_VARIABLE = 3


int_var = 5
float_var = 3.14
str_var = "Hello"
bool_var = True


a = 5
b = float(a)
print("Converted float:", b)


var = 10
print(type(var))


num1 = 10
num2 = 3
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)


print("Greater than:", num1 > num2)
print("Less than:", num1 < num2)
print("Equal to:", num1 == num2)
print("Not equal to:", num1 != num2)


a = 10
b = 3
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)





bool_var = True
print("Boolean variable:", bool_var)


a = True
b = False
print("Logical AND:", a and b)
print("Logical OR:", a or b)
print("Logical NOT of a:", not a)


x = 5
y = 10
print("Greater than:", x > y)
print("Less than or equal to:", x <= y)
print("Equal to:", x == y)
print("Not equal to:", x != y)

condition = True
if condition:
    print("Condition is True")
else:
    print("Condition is False")

def is_even(num):
    return num % 2 == 0

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))



a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

x = 5
x += 3
print("Value of x after += operation:", x)


print("Greater than:", a > b)
print("Less than:", a < b)
print("Equal to:", a == b)
print("Not equal to:", a != b)

print("Logical AND:", True and False)
print("Logical OR:", True or False)
print("Logical NOT:", not True)


list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("Identity check (is):", list1 is list2)
print("Non-identity check (is not):", list1 is not list2)



my_list = [1, 2, 3, 4, 5]
print("List:", my_list)


my_list.append(6)
print("After adding 6:", my_list)
my_list.remove(3)
print("After removing 3:", my_list)


my_list.sort()
print("Sorted list:", my_list)


squared = [x**2 for x in range(5)]
print("Squared values:", squared)


print("Length of list:", len(my_list))




num = 10
if num > 0:
    print("Number is positive")


num = -5
if num >= 0:
    print("Number is non-negative")
else:
    print("Number is negative")


score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


num = 12
if num > 0:
    if num % 2 == 0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")
else:
    print("Number is not positive")


a = 10
b = 5
max_num = a if a > b else b
print("Maximum number:", max_num)





count = 0
while count < 5:
    print("Count:", count)
    count += 1


num = 10
while True:
    if num == 0:
        break
    print("Current number:", num)
    num -= 1


num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print("Current number (with continue):", num)




my_list = [1, 2, 3, 4, 5]
index = 0
while index < len(my_list):
    print("Element at index", index, ":", my_list[index])
    index += 1




for i in range(5):
    print("Iteration:", i)


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)


for num in range(1, 6):
    print("Number:", num)


for i in range(3):
    for j in range(2):
        print("i:", i, " j:", j)


for i in range(3):
    print("Iteration:", i)
else:
    print("Loop completed successfully!")





def greet():
    print("Hello, welcome to Python!")

greet()

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Result of addition:", result)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("Is 7 a prime number?", is_prime(7))
print("Is 10 a prime number?", is_prime(10))


def greet(name="Guest"):
    print("Hello,", name)

greet("სანდრო")
greet()


def describe_person(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

describe_person(age=30, name="John", city="New York")
