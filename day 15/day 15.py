def initial_chars(fullname):
    splited_fullname = fullname.split(" ")
    

    firstname = splited_fullname[0]
    lastname = splited_fullname[1]

    result = firstname[0] + "." + lastname[0]

    print(result)


initial_chars("Davit Barbakadze")


def average_arithmetic(numbers_list):
    jami = sum(numbers_list)
    print(jami)
    result = jami / len(numbers_list)
    print(result)


average_arithmetic([1,2,3,4,5,6,7,8,9,])

palindrom = "david"
print(palindrom[::-1])
# not a palindrom

# palindrom2 = "racecar"
# print(palindrom2[::-1])
# #this is a plaindrom

#another version

# def is_palindrom(word):
#     reversed_word = ""

#     for i in range(len(word) -1, -1, -1):
#         reversed_word = reversed_word + word[i]

#     print(reversed_word)

def solution(string):
    reversed_word = "abtyv"

    for i in range(len(string) -1, -1, -1):
        reversed_word = reversed_word + string[i]

    print(reversed_word)


# is_palindrom("racecar")



def remove_spaces(word):
    word_without_space = ""
    for char in word:
        if char != " ":
            word_without_space = word_without_space + char

    print(word_without_space)

remove_spaces("Goal- Oriented- Academy ")




