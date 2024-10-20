even_list = []
odd_list2 = []

def summ(listn):
    for i in listn:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list2.append(i)
    sum_even = sum(even_list)
    sum_odd2 = sum(odd_list2)
    return(sum_even, sum_odd2)


print(summ([1,2,3,4,5]))

print(len([1,2,3,4,5]))


name = "datucha"
name_list = name.split(" ")
new_name = " ".join(name_list)

print(name_list)
print(new_name)

