def common_elements(array1, array2):
    return list(set(array1) & set(array2))

# მაგალითი
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

print(common_elements(array1, array2))  
