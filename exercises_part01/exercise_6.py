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
