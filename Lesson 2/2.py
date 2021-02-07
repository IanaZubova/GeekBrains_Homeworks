my_list = list(input('Insert values without spaces and commas: '))

k = 0

for i in range(int(len(my_list) / 2)):
    my_list[k], my_list[k + 1] = my_list[k + 1], my_list[k]

    k += 2

print(list(my_list))