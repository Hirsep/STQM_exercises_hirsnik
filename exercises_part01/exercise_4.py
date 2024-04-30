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