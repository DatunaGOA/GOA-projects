# 1. range() - რიცხვების სერიის შექმნა
print("range() ფუნქცია:")
for i in range(1, 10, 2):  # range(1, 10, 2) ანუ 1-დან 10-მდე, 2-2 ნაბიჯით
    print(i)  # Output: 1, 3, 5, 7, 9

# 2. len() - სიგრძის გამოთვლა
print("\nlen() ფუნქცია:")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"{fruit} - სიგრძე: {len(fruit)}")  # თითოეულ ხილს აქვს თავისი სიგრძე

# 3. sum() - რიცხვების ჯამი
print("\nsum() ფუნქცია:")
numbers = [1, 2, 3, 4]
total = sum(numbers)  # sum() ჯამავს ყველა რიცხვს
print(f"რიცხვების ჯამი: {total}")  # Output: 10

# 4. min() და max() - მინიმალური და მაქსიმალური მნიშვნელობები
print("\nmin() და max() ფუნქციები:")
numbers = [10, 20, 5, 15]
print(f"მინიმალური მნიშვნელობა: {min(numbers)}")  # Output: 5
print(f"მაქსიმალური მნიშვნელობა: {max(numbers)}")  # Output: 20

# 5. sorted() - რიცხვების ორგანიზება ზრდის მიხედვით
print("\nsorted() ფუნქცია:")
numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers)  # sorted() აწყობს რიცხვებს ზრდის მიხედვით
print(f"რიცხვები ზრდის მიხედვით: {sorted_numbers}")  # Output: [1, 2, 5, 9]

# 6. abs() - აბსოლუტური მნიშვნელობა
print("\nabs() ფუნქცია:")
values = [-1, 2, -3, 4]
for value in values:
    print(f"აბსოლუტური მნიშვნელობა {value}: {abs(value)}")  # Output: 1, 2, 3, 4

# 7. enumerate() - ინდექსი და შესაბამისი მნიშვნელობა
print("\nenumerate() ფუნქცია:")
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index} - {fruit}")  # Output: 0 - apple, 1 - banana, 2 - cherry

# 8. zip() - ორი სერიას ერთად კომბინაცია
print("\nzip() ფუნქცია:")
names = ['Alice', 'Bob', 'Charlie']
scores = [90, 85, 88]
for name, score in zip(names, scores):  # zip() აერთიანებს ამ სერიებს
    print(f"{name} - ქულა: {score}")  # Output: Alice - 90, Bob - 85, Charlie - 88

# 9. map() - ფუნქციის გამოყენება სერიაზე
print("\nmap() ფუნქცია:")
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(lambda x: x * 2, numbers))  # map() ორმაგებს თითოეულ რიცხვს
print(f"ორიდან გაორმაგებული რიცხვები: {doubled_numbers}")  # Output: [2, 4, 6, 8]

# 10. filter() - ფილტრაცია
print("\nfilter() ფუნქცია:")
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # filter() ფილტრავს მხოლოდ წყვილ რიცხვებს
print(f"წყვილი რიცხვები: {even_numbers}")  # Output: [2, 4]

# 11. any() და all() - სიმართლე
print("\nany() და all() ფუნქციები:")
values = [True, False, True]
print(f"any() ფუნქციის შედეგი: {any(values)}")  # Output: True (თუ რაიმე სიმართლეა)
print(f"all() ფუნქციის შედეგი: {all(values)}")  # Output: False (თუ ყველა სიმართლეა)

# 12. def - ფუნქციის შექმნა
print("\ndef - ფუნქცია შექმნა:")

# მარტივი ფუნქცია, რომელიც მისასალმებელი შეტყობინებას აბრუნებს
def greet(name):
    return f"გამარჯობა, {name}!"  # ფუნქცია აბრუნებს მისასალმებელს

# ფუნქციის გამოძახება
print(greet("დავითი"))  # Output: "გამარჯობა, დავით!"

# 13. ფუნქცია ორი პარამეტრით
def add_numbers(a, b):
    return a + b  # ფუნქცია ორი რიცხვის ჯამის დაბრუნება

print(f"რიცხვების ჯამი: {add_numbers(5, 7)}")  # Output: 12

# 14. return - ფუნქციის შედეგის დაბრუნება
print("\nreturn - ფუნქციის შედეგის დაბრუნება:")

# ფუნქცია, რომელიც დაბრუნებს კონკრეტულ შედეგს
def multiply(a, b):
    result = a * b
    return result  # შედეგი უბრუნდება

print(f"გამრავლებული რიცხვი: {multiply(3, 4)}")  # Output: 12

# 15. default პარამეტრები
print("\ndefault პარამეტრები:")
# ფუნქცია, სადაც პარამეტრისთვის მივიღებთ default მნიშვნელობას
def greet_person(name, greeting="გამარჯობა"):
    return f"{greeting}, {name}!"

print(greet_person("გიორგი"))  # Output: "გამარჯობა, გიორგი!"
print(greet_person("თამარი", "ბუნებრივი"))  # Output: "ბუნებრივი, თამარი"

# 16. lambda - ანონიმური ფუნქციები
print("\nlambda ფუნქცია:")
# lambda ფუნქცია, რომელიც აიღებს ორი რიცხვი და გამოითვლის მათი ჯამს
add = lambda x, y: x + y
print(f"lambda შედეგი: {add(3, 4)}")  # Output: 7

# 17. recursion - რიკურსია (ფუნქციის თვითგამეორება)
print("\nrecursion - რიკურსია:")
# ფაკტორიანტის გამოთვლა რიკურსიით
def factorial(n):
    if n == 0:  # ბაზის შემთხვევა
        return 1
    else:
        return n * factorial(n-1)  # თვითგამეორება

print(f"6-ის ფაკტორიანტი: {factorial(6)}")  # Output: 720

# 18. try/except - შეცდომების დამუშავება
print("\ntry/except - შეცდომების დამუშავება:")

# try/except გამოიყენება შეცდომის მოსაგვარებლად
try:
    result = 10 / 0  # აქ იქნება ZeroDivisionError
except ZeroDivisionError:
    print("შეცდომა! არ შეიძლება გაყოფა ნულიით.")
else:
    print("ყველაფერი წავიდა კარგად!")

# 19. break და continue
print("\nbreak და continue:")

for i in range(1, 10):
    if i == 5:
        break  # ციკლი დაიხურება, როდესაც i გახდება 5
    print(i)
    
# იგივე, მაგრამ continue-ის გამოყენებით:
print("\ncontinue:")
for i in range(1, 10):
    if i == 5:
        continue  # ციკლი გააგრძელებს ბრუნვას 5-ის გამოტოვებით
    print(i)





