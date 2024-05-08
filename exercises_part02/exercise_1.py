"""
### Exercise 1: Counting ###

Write a function count_a_number(numbers, number) that accepts a list of integers named
numbers and an integer named number as arguments. It counts the occurrence of the integer
number in the list and returns the count as an integer. Do not use-built-in functions! Use loops to
solve the problem.

"""


def count_a_number(numbers, number):
    count = 0
    for num in numbers:
        if num == number:
            count += 1
    return count


print(count_a_number([1, 3, 5, 7, 9, 1, 3, 5, 7, 9], 3))
