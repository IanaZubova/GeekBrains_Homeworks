def div():
    el_1 = int(input('Indicate element 1: '))
    el_2 = int(input('Indicate element 2: '))
    if el_2 == 0:
        print('Error, try again')
    result = el_1 / el_2
    return result

answer = div()

print(f'Answer - {answer}')