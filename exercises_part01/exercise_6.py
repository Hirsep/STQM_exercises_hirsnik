"""
### Exercise 6: Summarizer ###

Write a function sum_up(number1, number2) that accepts two integers and sums up every
integer between the two numbers including the given integers (inclusive). Check if the second
number is greater than the first and display a message if it’s not. The function returns the result as an
integer.
Example: if the function is called with 3 and 9, that is, sum_up(3, 9) the result is 42 because:
3 + 4 + 5 + 6 + 7 + 8 + 9 = 42

"""


def sum_up(number1, number2):
    total = 0
    if number2 < number1:
        yes_no = input("Your second number is lower than your first one do you want to swap them? (y/n)\n>>: ")
        if yes_no.lower() == "y":
            for number in range(number2, number1 + 1):
                total += number
        else:
            return "Numbers not swapped. Terminating process..."
        return int(total)
    else:
        for number in range(number1, number2 + 1):
            total += number
        return int(total)


print(sum_up(9, 3))
