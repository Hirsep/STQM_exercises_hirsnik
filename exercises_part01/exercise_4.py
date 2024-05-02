"""
### Exercise 4: Swap ###

Write a function swap_integers() that reads two integers from the user and prints them on the
console. Then the function swaps the integers in memory and prints the swapped integers again on
the console. If, for example, the first integer is x=10 and the second is y=20, x must have the value
20 after the swap (Hint: you can use a temporary variable). The function does not return anything.
Example output:
Please enter x: 10
Please enter y: 22
x=10
y=22
After swap:
x=22
y=10

"""


def swap_integers():
    while True:
        x = input("Please enter x: ")
        y = input("Please enter y: ")
        if not x.isnumeric() or not y.isnumeric():
            print("Only naturals numbers for age accepted.")
        else:
            x, y = int(x), int(y)
            break

    print(f"x = {x}\ny = {y}")
    z = x
    x = y
    y = z
    print(f"x = {x}\ny = {y}")


swap_integers()