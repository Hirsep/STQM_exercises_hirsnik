"""
### Exercise 3: Comparing list elements ###

Write a function compare_lists(list1, list2) that accepts two list as arguments. The
function looks for elements that the two lists have in common. It returns a list containing all those
elements. This list may be empty if there are no common elements.

"""


def compare_lists(list1, list2):
    compare = [element for element in list1 if element in list2]
    return compare


print(compare_lists(["e1", "e2"], ["e1", "e2"]))

