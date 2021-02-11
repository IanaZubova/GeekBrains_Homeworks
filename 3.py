list = [12, 23, 43, 15]

def my_func():
    return max(list)


print(my_func())

list.pop(list.index(max(list)))

print(my_func())