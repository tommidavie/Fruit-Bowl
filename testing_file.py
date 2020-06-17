from validations import validate_integer
import math


def get_string(m):
    my_string = input(m)
    return my_string


def single_loop_print(F):
    for i in range(0, len(F)):
        output = "{:10} {:10}".format(F[i][0], F[i][1])
        print(output)


def fill_a_fruit_bowl(F):
    fruit_name = get_string("What fruit group would you like to add? : ")
    fruit_number = validate_integer("What is the quantity of this fruit? : ", 0, 500)
    temp_list = (fruit_name, fruit_number)
    F.append(temp_list)
    output = "You have now added {} {} to your fruit bowl".format(fruit_number, fruit_name)
    print(output)


def print_indexes_too(L):
    for i in range(0, len(L)):
        output ="{:3} : {:10}  {:10}".format(i,L[i][0], L[i][1])
        print(output)


def update_fruit(F):
    print_indexes_too(F)
    index_number = validate_integer("Please chose the index number you would like to edit: ", 0, math.inf)
    negative_positive = get_string("Would you like to add (A) or subtract (S) from this fruit group: ")
    if negative_positive == "A":
        change = validate_integer("How much would you like to add to this quantity: ", 0, 500)
        F[index_number][1] += change
        output = "You now have added {} {} to your fruit bowl".format(change, F[index_number][0])
        print(output)
    elif negative_positive == "S":
        change = validate_integer("What quantity would you like to subtract from this fruit group: ", 0, 500)
        F[index_number][1] -= change
        output = "You now have subtracted {} {} to your fruit bowl".format(change, F[index_number][0])
        print(output)
    else:
        print("You have not entered a sufficient answer. Please try again.")


def menu():

    fruit_list = []

    full_bowl = [
        ["Oranges", 5],
        ["Apples", 7],
        ["Watermelon", 3],
        ["Strawberries", 29]
    ]

    #fruit_list = full_bowl

    my_menu = [("R", "Review"),
               ("Q", "Quit"),
               ("A", "Add new fruit"),
               ("U", "Update Your Fruit Bowl")
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
        elif option == "U":
            if len(fruit_list) == 0:
                print("There is nothing in your fruit bowl.")
            else:
                update_fruit(fruit_list)
        else:
            print("That is not a valid option, please try again")


if __name__ == "__main__":
    menu()
