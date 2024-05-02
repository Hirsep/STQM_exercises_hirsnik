"""
### Exercise 8: String check ###

Write a function check_string(text) that accepts a string and checks if it begins OR ends with
the character “a”. Use built-in string methods of python. A list with all methods can be found here:
https://docs.python.org/3/library/stdtypes.html#string-methods
The function returns True if the string begins or ends with an “a”. The function should work for
lower and upper case strings.

"""


def check_string(text):
    text = text.lower()
    if text.endswith("a") or text.startswith("a"):
        return True
    return False


print(check_string("asd"))
print(check_string("wasd"))
