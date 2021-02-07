statement = input('Insert a few words: ')

result = statement.split()

for ind, el in enumerate(result, 1):
    print(ind, el [:10])