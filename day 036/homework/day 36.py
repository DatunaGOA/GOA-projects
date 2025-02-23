
list_of_dicts = []

my_dict = {'name': 'davit', 'age': 13}
list_of_dicts.append(my_dict)

friend_dict = {'name': 'Sandro', "age" : 15}
list_of_dicts.append(friend_dict)

family_member_dict = {'name': 'Barbare', 'age': 6}
list_of_dicts.append(family_member_dict)

random_dict = {"nika doxnadze" : 13, "nina jokhadze" : 16}
list_of_dicts.append(random_dict)

for dictionary in list_of_dicts:
    print(dictionary)


#kata 1

def user_contacts(users):
    contacts = {}
    for user in users:
        if len(user) == 2:
            contacts[user[0]] = user[1]
        else:
            contacts[user[0]] = None
    return contacts





#kata 2

def fillable(stock, merch, n):
    if merch in stock:
        return stock[merch] >= n
    else:
        return False


