# # 1. თქვენ მუშაობთ სიაზე, სადაც მოცემულია ნებისმიერი მონაცემი, მაგალითად "hello", 4.14, True და ა.შ. თქვენი დავალებაა,
#  რომ ამ სიაში მოცემული მთელი რიცხვების ჯამი დაბეჭდოთ ტერმინალში.

# # 2. თქვენ მუშაობთ რიცხვების სიაზე, შესაძლოა გქონდეთ როგორც მთელი რიცხვები, ასევე 
# ათწილადები. დავალებაა, რომ დააბრუნოთ სიის რიცხვების ჯამი, მაგრამ  ამ ჯამში არ შევა მაქსიმალური 
# და მინიმალური მნიშვნელობები.

# # 3. მომხმარებელს შემოატანინეთ დადებითი მთელი რიცხვი. შემდეგ გამოიყენეთ ციკლი, სიაში
#  დაამატეთ ყველა ამ რიცხვის გამყოფი და დაბეჭდეთ ეს სია.

# # 4. მომხმარებელს შემოატანინეთ სიტყვა და შემდეგ განიხილეთ ამ სიტყვის ყველა ასო. lowercase 
# გადააკეთეთ uppercase-ად, ხოლო uppercase კი lowercase-ად.

# # 5. თქვენ გადმოგეცემათ მთელი რიცხვების სია. დავალებაა, რომ ყველაზე ხშირად განმეორებადი 
# რიცხვის რაოდენობა დააბრუნოთ ამ სიიდან. ამ დავალების სია აიღეთ ქვემოთ მოცემული test case-იდან.

list = [1, 2, 3, False, 1.5, 3.14, 5,]
total_sum = 0

for item in list:
    if isinstance(item, int):
        total_sum += item
print("The sum of integers in the list is:", total_sum)
#2
def sum_without_extremes(numbers):

    if len(numbers) > 2:
        numbers.remove(max(numbers))
        numbers.remove(min(numbers))
    
    return sum(numbers)

#3
numbers_list = [5, 11, 2, 20, 4.4, 6.6] #7


print("The sum of the numbers excluding the maximum and minimum values is:", sum_without_extremes(numbers_list))


number = int(input("please enter a positive number: "))

divisors = [i for i in range(1, number + 1) if number % i == 0]

print(divisors)

#4
word = input("please enter a word containing uppercase letters: ")
converted_word = ''.join([char.lower() if char.isupper() else char.upper() for char in word])
print(converted_word)


#5


num = [1, 1, 1, 1, 3, 4, 5, 6]


counts = {}
for num in num:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

most_common = max(counts, key=counts.get)

print(most_common)
