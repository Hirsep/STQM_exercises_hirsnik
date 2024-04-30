def name_age():
    name = input("What is your name? >>: ")
    while True:
        age = input("What is your age? >>: ")
        if not age.isnumeric():
            print("Only naturals numbers for age accepted.")
        else:
            age = int(age)
            break
    print(f"Hello, {name.capitalize()}. You are {age} years old.")
    print("Hello {}. You are {} years old.".format(name.capitalize(), age))
    print("Hello " + name.capitalize() + ". You are " + str(age) + " years old.")


name_age()

