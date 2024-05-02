"""
### Exercise 5: Modulo check ###

Write a function check_numbers(number1, number2) that accepts two arguments. The
function checks if any of the numbers is divisible by 6 and if both are divisible by 10. The function
does return true if both conditions are true. Hint: Use the modulo operator.
Example output:
Number 1: 6
Number 2: 10
One number is divisible by 6
Both numbers are not divisible by 10

"""


def check_numbers(number1, number2):

    print(f"Number 1: {number1}\nNumber 2: {number2}")

    if number1 % 6 == 0 or number2 % 6 == 0:
        print("One number is divisible by 6")
        if number1 % 10 == 0 and number2 % 10 == 0:
            return True
        else:
            print("Both numbers are not divisible by 10")
    return False


check_numbers(6, 10)
