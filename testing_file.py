def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def single_loop_print(F):
    for i in range(0, len(F)):
        output = "{:10} {:10}".format(F[i][0], F[i][1])
        print(output)

def fill_a_fruit_bowl(F):
    fruit_name = get_string("What fruit group would you like to add? : ")
    fruit_number = get_integer("What is the quantity of this fruit? : ")
    temp_list = (fruit_name, fruit_number)
    F.append(temp_list)
    output = "You have now added {} {} to your fruit bowl".format(fruit_number, fruit_name)
    print(output)

def menu():

    fruit_list = []
    my_menu = [("R", "Review"),
               ("Q", "Quit"),
               ("A", "Add new fruit")
               ]

    run = True
    while run == True:
        for i in range(0, len(my_menu)):
            print("{:3} : {}".format(my_menu[i][0], my_menu[i][1]))

        option = get_string("Please choose an option: ")
        if option == "R":
            single_loop_print(fruit_list)
        elif option == "A":
            fill_a_fruit_bowl(fruit_list)
        elif option == "Q":
            run = False
            print("You have now exited the loop")
        else:
            print("That is not a valid option, please try again")


if __name__ == "__main__":
    menu()
