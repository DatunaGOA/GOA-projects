#1. შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების კოლექცია. თქვენ უნდა განიხილოთ 
# მთლიანი კოლექცია: თუ რიცხვი იქნება მთელი - გაამრავლეთ ორზე, ხოლო თუ რიცხვი იქნება 
# ათწილადი - გაამრავლეთ ოთხზე. ყველა რიცხვი დაამატეთ ახალ სიაში და დააბრუნეთ ეს სია.

#[1, 1.5, 2, 2.5] -> [2, 6, 4, 10]



 

def collection(col):
    new_col = []
    for num in col:
        if isinstance(num, int):
            new_col.append(num * 2)
        elif isinstance(num, float):
            new_col.append(num * 4)
    return new_col

col = [1, 1.5, 2, 2.5]
result = collection(col)
print(result) 

#შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. ლუწ ინდექსებზე მყოფი სახელები გადაიყვანეთ uppercase-ში, 
# ხოლო კენტ ინდექსებზე მყოფნი კი lowercase-ში.
#["chad1", "chad2", "chad3", "chad4"] -> ["CHAD1", "chad2", "CHAD3", "chad4"] 

list = ["chad1", "chad2", "chad3", "chad4"]
list.uppercase([0])
print(list)