"""
### Exercise 5: Computer description ###

Write a function describe_computer(computer) that accepts a dictionary named
computer as argument. The given dictionary contains the keys “Type”, “Brand” and “Price”.
The function prints out the values of the dictionary in the following format:
You have a TYPE from BRAND that costs PRICE€.
The capitalized words like TYPE and BRAND represent the values assigned to the keys in the
dictionary.
Then the function adds the key “OS” to the dictionary and defaults it to “Linux”. Afterwards it
prints the dictionary to the console.
Example:
my_notebook = {'Type': 'Notebook', 'Brand': 'Dell', 'Price': 2000}
describe_computer(my_notebook)
Example output:
You have a Notebook from Dell that costs 2000€.
{'Type': 'Notebook', 'Brand': 'Dell', 'Price': 2000, 'OS': 'Linux'}
If one of the keys is not present, the value used in the output defaults to a custom text like “unknown
brand” for the key “Brand”.
The function does not return anything.

"""


def describe_computer(computer):
    computer['OS'] = 'Linux'
    computer.setdefault('Type', 'unknown Type')
    computer.setdefault('Brand', 'unknown Brand')
    computer.setdefault('Price', 'unknown Price')
    computer_order = ['Type', 'Brand', 'Price', 'OS']
    computer = {key: computer[key] for key in computer_order if key in computer}
    print(computer)


my_notebook = {'Brand': 'Dell', 'Price': 2000}
describe_computer(my_notebook)
