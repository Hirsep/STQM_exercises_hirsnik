"""
### Exercise 2: Playing with lists ###

Write a function play_with_lists(numbers, number) that accepts a list of integers
named numbers and an integer named number as arguments. Use built-in list functions to achieve
the following:
 Print out the list in reverse order but leave the original list in order
 Replace the given integer number within the list with the number 1 and print it on the
console
 Print out a sorted version of the list in descending order
Don’t forget that lists are mutable. You probably will have to make a copy if you want the leave the
original list untouched. Investigate the difference between using the build-in function
sorted(list) and the sort function of the class list. Write a comment why you chose the
sorting function you used.
The function does not return anything

"""


def play_with_lists(numbers, number):
    reversed_numbers = numbers[:]
    reversed_numbers = reversed_numbers[::-1]   #reversed_numbers.reverse() also possible

    print(f"Original list: {numbers}\nReversed list: {reversed_numbers}")

    replaced_numbers = [1 if item == number else item for item in numbers]
    print(f"Replaced 1 with {number} in {numbers}\n{replaced_numbers}")

    copy_of_numbers = numbers[:]
    copy_of_numbers.sort()                  #.sort() modifies the original list and therefore a copy has to be created
    print(copy_of_numbers)
    print(sorted(numbers, reverse=True))    #use sorted() to create a new list without modifying the original


play_with_lists([1, 3, 5, 7, 9, 1, 3, 5, 7, 9], 3)
