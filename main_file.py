def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def single_loop_print(L):
    for i in range(0, len(L)):
        output = "{:10} {:10}".format(L[i][0], L[i][1])
        print(output)

def menu():

    my_list = [
        ["Oranges", "4"],
        ["Apples", "5"],
        ["Mangoes", "30"],
        ["Watermelon", "4"],
        ["Blueberries", "348"]
        ]

    my_menu = [("R", "Review"),
               ("Q", "Quit")]

    run = True
    while run == True:
        for i in range(0, len(my_menu)):
            print("{:3} : {}".format(my_menu[i][0], my_menu[i][1]))
        option = get_string("Please choose an option: ")
        if option == "R":
            single_loop_print(my_list)
        elif option == "Q":
            run = False
            print("Thanks for playing")
        else:
            print("That is not a valid option")


if __name__ == "__main__":
    menu()





