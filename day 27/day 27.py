#1
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

#2
def conv_names(names):
    for i in range((names)):
        if i % 2 == 0:
            names[i] = names[i].upper()
        else:
            names[i] = names[i].lower()
    return names

names = ["chad1", "chad2", "chad3", "chad4"]
converted_names = conv_names(names)
print(converted_names)



#3

def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized_sentence = ' '.join(word.capitalize() for word in words)
    return capitalized_sentence

sentence = "hello, this is goa"
resul = capitalize_sentence(sentence)
print(resul) 


#4
def manual_pop(collection, remove_index):

    if remove_index >= len(collection):
        return "Index out of range"
    resultt = []
    for index in range(len(collection)):
        if index != remove_index:
            resultt.append(collection[index])
    return resultt
print(manual_pop(["Luka", "lile"], 1))


#5

def remove_duplicates(lst):
    return list(set(lst))

example_list = [1, 1, 1, 2, 3, 4]
resulttt = remove_duplicates(example_list)
print(resulttt)


#6


def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list
example_list = [1, 1, 1, 2, 3, 4]
result1 = remove_duplicates(example_list)
print(result1) 


#7

def count_occurrences(collection, word):
    return collection.count(word)


example_list = [1, 1, 1, 2, 3, 4]
target_word = 1
result2 = count_occurrences(example_list, target_word)
print(result2) 


#8
def remove_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result3 = remove_even_numbers(example_list)
print(result3)


#9
def merge_lists(list1, list2):
    return list1 + list2
list1 = [1, 5, 8]
list2 = [2, 3, 4]
result = merge_lists(list1, list2)
print(result)

#10

def remove_duplicates(collection):
    return list(set(collection))
example_list = [1, 1, 1, 2, 3, 4]
result = remove_duplicates(example_list)
print(result) 