
def manual_pop(list, index=None):
    if index is not None:
        if 0 <= index < len(list):
            return list[:index] + list[index + 1:]
        else:
            print("Index out of range. Returning original list.")
            return list
    else:
        if list:
            return list[:-1]
        else:
            print("List is empty. Returning original list.")
            return list
num_list = [1, 2, 3, 4, 5]
print(manual_pop(num_list))  
print(manual_pop(num_list, 2))  


def manual_count(list, element=None):
    if element is not None:
        count = 0
        for item in list:
            if item == element:
                count += 1
        return count
    else:
        if list:
            average = int(sum(list) / len(list))
            return average
        else:
            print("List is empty. Cannot calculate average.")
            return None
num_list2 = [10, 11, 10, 10]
print(manual_count(num_list2))
print(manual_count(num_list2, 3))  



def manual_min(lst=None):
    if lst is None:
        lst = list(range(1, 11))  

    minimum_value = lst[0]
    for num in lst:
        if num < minimum_value:
            minimum_value = num

    return minimum_value


custom_list = [10, 13, 9, 5]
print("Minimum value in custom list:", manual_min(custom_list))


print("Minimum value in default list:", manual_min())

def manual_max(i=None):
    if i is None:
        i = list(range(1, 11))  

    max_value = i[0]  
    for num in i:
        if num > max_value:
            max_value = num

    return max_value

custom_list2 = [10, 13, 9, 5]
print("Maximum value in custom list:", manual_max(custom_list2))

print("Maximum value in default list:", manual_max())
