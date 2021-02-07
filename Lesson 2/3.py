month = int(input('Indicate the number of a month: '))

seasons = dict(Winter=[1, 2, 12],
               Spring=[3, 4, 5],
               Summer=[6, 7, 8],
               Autumn=[9, 10, 11]
               )

for key in seasons.keys():
    if month in seasons[key]:
        print(key)