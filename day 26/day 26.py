#მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ დაბეჭდეთ lower, upper, capitalize ვარიანტებად.
name = input("please enter your name: ")
print(name.capitalize())
print(name.lower())
print(name.upper())

# შექმენით ფუნქცია, სახელად find_index,
# რომელსაც გადაეცემა სთრინგი და საპოვნელი ასო. თქვენი დავალებაა, რომ გადაცემულ სთრინგში არსებული ასოს ინდექსი დააბრუნოთ.

find_index = "Goal Oriented Academy".find("d")
print(find_index)

# def keyword'ის გამოყენებით შექმენით len()'ის მსგავსი ფუნქცია ( ფუნქცია რომელიც გამოიტანს რამდენი ელემენტია list'ში).
def keyword(my_list):
    count = 0
    for i in my_list:
        count += 1
    return count

print(keyword([1, 2, 3, 4, 5]))

# გატესტეთ insert, pop, len, append და ახსენით თქვენი სიტყვებით თუ რას აკეთებს.

test = [1, 2, 3, 4, 5, 6]
test2 = test.pop(3)
print(test2)
print(test)
# პოპის მეთოდი Python-ში გამოიყენება იმისათვის, რომ ელემენტი ამოიღონ
# მითითებულ პოზიციაზე სიაში ან ლექსიკონში და დააბრუნონ იგი.

ins = [1, 3, 4, 5,]
ins2 = ins.insert(1, 2)
print(ins2)
print(ins)

#python-ის insert() ფუნქცია სიაში გამოიყენება ელემენტის ჩასართავად მომხმარებლის მიერ მითითებულ ნებისმიერ ინდექსში.

len1 = [2, 3, 4, 5, 6, 7, 8]
print(len(len1))

#ფუნქცია len() არის პითონის ერთ-ერთი ჩაშენებული ფუნქცია. ის აბრუნებს ობიექტის სიგრძეს

app = [1, 2, 3, 4, 5, 6, 7, 8, 9]
app.append(10)
print(app)

# #Python-ში append() მეთოდი ამატებს ერთ ელემენტს არსებული სიის ბოლოს.

