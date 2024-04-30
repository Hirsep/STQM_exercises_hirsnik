def sequence(number):
    if number > 9 or number < 0:
        return print('Error: Only numbers in range 0 - 9 are accepted for function "sequence".')
    for z in range(10):
        if z != number:
            print(z, end=" ")


sequence(10)