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
