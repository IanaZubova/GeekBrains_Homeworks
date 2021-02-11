new_elements = 0

try:

    while True:
        elements = map(int, input('Provide numbers: ').split())

        for i in elements:
            new_elements += i

        print(new_elements)

except ValueError:

    print(new_elements)