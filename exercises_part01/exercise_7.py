"""
### Exercise 7: Sequencer ###

Write a function sequence(number) that accepts an integer as argument. It then checks if the
given number is an integer between 0 and 9 (inclusive) and prints an error message if it’s not. In case
the given number is between 0 and 9, the function prints the sequence of number from 0 to 9 on the
console without the given number. The function does not return anything.
For sequence(5)your output should look like the following:
0 1 2 3 4 6 7 8 9

"""


def sequence(number):
    if number > 9 or number < 0:
        return print('Error: Only numbers in range 0 - 9 are accepted for function "sequence".')
    for z in range(10):
        if z != number:
            print(z, end=" ")


sequence(10)

#def sequence(number):
#    if number > 9 or number < 0:
#        print('Error: Only numbers in range 0 - 9 are accepted for function "sequence".')
#        return
#    z = 0
#    while z < 10:
#        if z != number:
#            print(z, end=" ")
#        z += 1
