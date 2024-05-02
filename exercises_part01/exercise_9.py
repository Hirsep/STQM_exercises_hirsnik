"""
### Exercise 9: ASCII Art ###

Write a function triangle(rows) that accepts an integer and prints out a triangle of stars with
spaces in between them with the height of the given integer.
Example: triangle(4) would result in a triangle with 4 rows
The function does not return anything.
"""


def triangle(rows):
    for number in range(1, rows + 1):
        stars = number
        print(stars * "* ")


triangle(4)


#def triangle(rows):
#    number = 1
#    while number <= rows:
#        stars = ""
#        count = 0
#        while count < number:
#            stars += "* "
#            count += 1
#        print(stars)
#        number += 1
