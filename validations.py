def validate_integer(m, min, max):
    while True:
        try:
            change = int(input(m))
        except ValueError:
            print("Your entry must be a number. Please try again.")
            continue
        if change <= min:
            print("Your entry is too small, it must be above -1. Please try again.")
        elif change > max:
            print("Your entry is too big, it must be below 501. Please try again.")
        else:
            return change

if __name__ == "__main__":
    change = validate_integer("Please enter your number: ", 0, 5)
    print(change)