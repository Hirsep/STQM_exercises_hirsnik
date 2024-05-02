"""
### Exercise 3: Formatting ###

Write a function name_age() that accepts the name and age of a person. It then prints it on the
console in the following format:
Hello, NAME. You are AGE years old.
The function does not return anything. Use the input() function to read the name and age as a
string and an integer. Use at least three different methods to format the output, e.g. concatenation,
String format(), f-strings, … That is, print the greeting three times using different formatting
methods which produce the same output.
Your output should look something like the following:
Hello, Georg. You are 46 years old.
Hello, Georg. You are 46 years old.
Hello, Georg. You are 46 years old.

"""


def name_age():
    name = input("What is your name? >>: ")
    while True:
        try:
            age = int(input("What is your age? >>: "))
            break
        except ValueError:
            print("Only numbers accepted for age.")

    print(f"Hello, {name.capitalize()}. You are {age} years old.")
    print("Hello {}. You are {} years old.".format(name.capitalize(), age))
    print("Hello " + name.capitalize() + ". You are " + str(age) + " years old.")


name_age()

