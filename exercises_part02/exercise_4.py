"""
### Exercise 4: No duplicates! ###

Write a function remove_duplicates(items) that accepts a list of strings named items as
argument and removes all duplicate values from the list. There is an easy way to do this using
another container. Search for this way and implement it.
Then write another function named remove_duplicates_my_way(items). This time find a
way to accomplish the task without using another container.
Both functions return the list of strings without duplicates.

"""


def remove_duplicates(items):
    return list(set(items))


def remove_duplicates_my_way(items):
    items.sort()
    i = 0
    while i < len(items) - 1:
        if items[i] == items[i + 1]:
            del items[i]
        else:
            i += 1
    return items


print(remove_duplicates(["a", "b", "a", "c", "b", "a"]))
print(remove_duplicates_my_way(["a", "b", "a", "c", "b", "a"]))
