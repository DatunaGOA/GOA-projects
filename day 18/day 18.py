
name = input("please enter your name: ")

lowercase_name = name.lower()

if name == lowercase_name:
    print("The name matches its lowercase variant.")
else:
    print("The name does not match its lowercase variant.")




counter = 0

while True:
    random_word = input("Enter any word you would like: ")
    counter += 1
    is_lowercase = False

    for letter in random_word:
        if letter.islower():
            is_lowercase = True
            break

    if is_lowercase:
        print("The word contains lowercase letters. Please enter the word again.")
    else:
        break
    print("You entered the word without any lowercase letters after", counter, "attempt(s).")


word = input("Enter a random word: ")
result = ""

for index, letter in enumerate(word):
    if index % 2 == 0: 
        result += letter.upper()
    else: 
        result += letter.lower()

print("Converted word:", result)



my_name = "david".capitalize()
my_lastname =  "barbakadze".capitalize()

print(my_name + " " + my_lastname)


user_name = input("please eneter your name: ")
user_lastname = input("please enter your lastname: ")

initials = user_name.capitalize()
initials2 = user_lastname.capitalize()
print(initials[0] + "." + initials2[0])


word3 = input("Enter a word: ")
search_letter = input("Enter the letter to search for: ")

index = word3.find(search_letter)

if index != -1:
    print("Index of the first occurrence of", search_letter, "in the word:", index)
else:
    print("The letter", search_letter, "does not exist in the word. Index: -1")