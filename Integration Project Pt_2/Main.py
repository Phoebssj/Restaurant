"""
# An integration project on what I've learn so far, In a Restaurant theme.
This program will provide a menu and will ask the user for inputs for dish,
drink and quantity. It will provide a calculation of the cost of the entire
meal
ask the user to oay and ask for a tip.

The code will start with the welcome customer function, where the customer
will be
greeted.
"""
__author__ = "Sheryll Jacquet"


def appetizer_request():
    """
    These lines of code give an option for customers to decline or
    Decide for having a snack before their main dish.
    This also checks if they type the correct option and quantity.
    """
    ask_for_appetizer = input(
        "Would you like an appetizer. Type Yes or No.: ")
    if ask_for_appetizer == "yes" or ask_for_appetizer == "Yes":
        appetizer_menu = open('Appetizer.txt')
        for appet_line in range(6):
            am = appetizer_menu.readline()
            print(am)  # If yes a section of the menu will be printed for them.
            """
            The code if from Hackerrank #5 Good Letter Input. But in 
            this case checks if they input the proper that correlates
            to the menu. It will loop until you type the number that 
            correlates to the appetizer then moves to qt.
            """
        appet_choice = input("What appetizer would you like? "
                             "Please type the number "
                             "that corresponds to appetizer on the menu.: ")
        appet_qt = 0
        while not (appet_choice == "1" or
                   appet_choice == "2" or appet_choice == "3"):
            appet_choice = input("What appetizer would you like? Please type "
                                 "the number "
                                 "that corresponds to the appetizer: ")
        if appet_choice == "1" or appet_choice == "2" or appet_choice == "3":
            while True:
                try:
                    appet_qt = int(input("How many would you like?: "))
                    break
                except ValueError:
                    print("Improper Input. Please provide a "
                          "whole number input.")
            if appet_qt < 0:
                print("Improper Input. Please provide a whole number.")
                while True:
                    try:
                        appet_qt = int(input("How many would you like?: "))
                        break
                    except ValueError:
                        print("Improper Input. Please provide a positive whole"
                              "number.")
        else:
            print("Invalid Input. Please Try again.")
        return [appet_choice,
                appet_qt]
        # Since we can't get the inputs from user my uncle
        # suggested to use a list instead that way we can call their value
    elif ask_for_appetizer == "no" or ask_for_appetizer == "No":
        print("Okay let's move on to the next selection")
        return None
        # That's where the main dish menu will be printed.
    else:
        print(
            "Sorry " + ask_for_appetizer + "\n Is not a proper input.\n" +
            "Please provide a proper input")
        return appetizer_request()
        # This option loops back in order to get a proper answer.


def calculate_total(total_1, total_2, total_3):
    """
    This function calculates the total price of the entire meal.
    TA Mr. Smith helped me for this function.
    """
    total = (total_1 + total_2 + total_3) + (59 % 6) / 100
    return total


def welcome_customer():
    """
    This function can be called each time we refer to the current customer.
    """
    customer_name = input("Enter your name: ")
    return customer_name


# once the name is called back the print statement will greet the customer

customer = welcome_customer()
print(
    "Welcome" + customer + "to Spunky Joe's Cuisine Restaurant!"
                           "Here is the Menu for tonight!:")

full_menu = open('FullMenu.txt')
for fm_line in range(23):
    fm = full_menu.readline()
    print(fm)

"""These variables represent the appetizers section of the menu and 
their their prices. appet are the name of the dishes and appet_#_price are
their cost. The appet are listed in the dictionary that will be called 
later on. The idea of dictionary was an idea from my teammate Bradley and 
from the TA Ms. Rachel"""

appet = {"1": "Garlic Bread Crumpets",
         "2": "Cesar Salad with Dressing",
         "3": "Chips with Jalepeño Dip"}
appet_1_price = 4.49
appet_2_price = 5.50
appet_3_price = 3.49

"""
These variables represent the main dish section of the menu and 
their their prices. main_dish are the name of the dishes and 
main_dish_#_price are their cost. The main dish are listed in the dictionary 
that will be called later on. The idea of dictionary was an 
idea from my teammate Bradley and from the TA Ms. Rachel
"""

main_dish = {"1": "Filet Mignon",
             "2": "Fruit Salad with Grilled Fish",
             "3": "Garlic Alfredo with Shrimp, Peppers & Onions"}
main_dish_1_price = 15.49
main_dish_2_price = 13.50
main_dish_3_price = 14.49

"""
# These are variables to represent the beverage section of the menu.
# bev represents the names of each drink and bev_#_price are there prices.
# The beverages are listed within the dictionary. The idea of using the 
# dictionary was an idea from my teammate Bradley and from the TA Ms. Rachel"
"""

bev = {"1": "Apple Cider",
       "2": "Sparkling Water",
       "3": "Grape Wine"}
bev_1_price = 5.00
bev_2_price = 2.50
bev_3_price = 6.49


def main():
    """
    This function then goes through the process of asking for the main dish
    and beverage of choice. Then calculates  the total of each
    """

    """
    Another issue we ran into was making sure the variables existed.
    So we used an if statement to verify if the appetizer options are mentioned
    that way it's represented as new variables. If not it will be ignored and
    will move on to the next section. This idea was from my uncle.
    """
    appet_chosen = None
    appet_chosen_qt = None
    appet_list = appetizer_request()
    if appet_list:
        for i in range(len(appet_list)):
            appet_chosen = appet_list[0]
            appet_chosen_qt = int(appet_list[1])

    """ This code opens the text file for the main dish"""
    main_menu = open('mainmenu.txt')
    for line_md in range(6):
        mm = main_menu.readline()
        print(mm)

    """
    Then the code then verifies whether or not you type the correct option.
    If not, it will loop. 
    The next code also verifies thr number quantity as well.
    If you type a string or float for qt it will inform the user.
    and prompt them to type a proper input 
    This code is from Hackerrank #5 Good Letter Input. 
    """
    # If the user types a negative for main_dish_qt It will prompt the user to
    # enter a positive number.

    main_dish_qt = 0
    main_dish_choice = input("Main Dish of choice? Please type the "
                             "number that corresponds to the Main Dish: ")
    while not (main_dish_choice == "1" or
               main_dish_choice == "2" or main_dish_choice ==
               "3"):
        main_dish_choice = input("Main Dish of choice? Please type the "
                                 "number that corresponds to the Main Dish: ")
    if main_dish_choice == "1" or main_dish_choice == "2" \
            or main_dish_choice == \
            "3":
        while True:
            try:
                main_dish_qt = int(
                    input("How many servings would you like?: "))
                break
            except ValueError:
                print("Improper Input. Please provide a whole number input.")
        if main_dish_qt < 0:
            print("Improper input. Please input a whole number.")
            while True:
                try:
                    main_dish_qt = int(input("How many servings "
                                             "would you like?: "))
                    break
                except ValueError:
                    print("Improper input. Please input "
                          "a positive whole number.")

    """ This code opens the text file for Beverages"""
    beverage_menu = open('Beverage.txt')
    for line_bev in range(8):
        bm = beverage_menu.readline()
        print(bm)

    """
    Then the code then verifies whether or not you type the correct option.
    If not, it will loop. 
    The next code also verifies thr number quantity as well.
    If you type a string or float for qt it will inform the user. 
    This code is from Hackerrank #5 Good Letter Input. 
    It they type in a negative number it will prompt to input a positive 
    integer
    """

    bev_choice = input("Beverage of Choice? Please type the number that "
                       "corresponds to the beverage.: ")
    bev_qt = 0

    while not (bev_choice == "1" or bev_choice == "2" or bev_choice == "3"):
        bev_choice = input("Beverage of Choice? Please type the number that "
                           "corresponds to the beverage.: ")
    if bev_choice == "1" or bev_choice == "2" or bev_choice == "3":
        while True:
            try:
                bev_qt = int(input("How many servings would you like?: "))
                break
            except ValueError:
                print("Improper Input. Please provide a whole number input.")
    if bev_qt < 0:
        print("Improper Input please provide a Positive whole number.")
        while True:
            try:
                bev_qt = int(input("How many servings would you like?: "))
                break
            except ValueError:
                print("Improper Input. Please provide a whole number input.")

    # Find out which appetizer the customer chose and what's the total price.
    # Recalling from the previous list this will verify if the list exist.
    # If it does we can call the option of the appetizer
    # and it qt in order to to calculate the
    # total price of the appetizer.
    # If not it will skip the calculations for appetizers
    # and move on to the main dish calculations.

    appet_total = 0
    if appet_list:
        if appet_chosen == "1":
            appet_total = appet_1_price * appet_chosen_qt
            print('You purchased {0}, {1}, for ${2}.'.format
                  (appet_chosen_qt, appet["1"], appet_total))
        elif appet_chosen == "2":
            appet_total = appet_2_price * appet_chosen_qt
            print('You purchased {0}, {1}, for ${2}.'.format
                  (appet_chosen_qt, appet["2"], appet_total))
        elif appet_chosen == "3":
            appet_total = appet_3_price * appet_chosen_qt
            print('You purchased {0}, {1}, for ${2}.'.format
                  (appet_chosen_qt, appet["3"], appet_total))
        else:
            print(
                "We don't have the appetizer that you mentioned, "
                "look back at the menu.")

    # Find out which main dish the customer chose and what's the price.
    main_dish_total = 0

    if main_dish_choice == "1":
        main_dish_total = main_dish_1_price * main_dish_qt
        print('You purchased {0}, {1}, for ${2}.'.format
              (main_dish_qt, main_dish["1"], main_dish_total))
    elif main_dish_choice == "2":
        main_dish_total = main_dish_2_price * main_dish_qt
        print('You purchased {0}, {1}, for ${2}.'.format
              (main_dish_qt, main_dish["2"], main_dish_total))
    elif main_dish_choice == "3":
        main_dish_total = main_dish_3_price * main_dish_qt
        print('You purchased {0}, {1}, for ${2}.'.format
              (main_dish_qt, main_dish["3"], main_dish_total))
    else:
        print(
            "we don't have the main dish that you mentioned, "
            "look back at the menu.")

    # Find out which beverage the customer chose and what's the price.
    bev_total = 0

    if bev_choice == "1":
        bev_total = bev_1_price * bev_qt
        print('You purchased {0}, {1}, for ${2}.'.format
              (bev_qt, bev["1"], bev_total))
    elif bev_choice == "2":
        bev_total = bev_2_price * bev_qt
        print('You purchased {0}, {1}, for ${2}.'.format
              (bev_qt, bev["2"], bev_total))
    elif bev_choice == "3":
        bev_total = bev_3_price * bev_qt
        print('You purchased {0}, {1}, for ${2}.'.format
              (bev_qt, bev["3"], bev_total))
    else:
        print(
            "we don't have the beverage that you mentioned, "
            "look back at the menu.")

    # Find out the total we should charge the costumer. As it's calculated
    # by the function.
    cost = calculate_total(appet_total, main_dish_total, bev_total)
    print("Your total cost for this dinner is $", format(cost, '.2f'), sep='')

    # This input allows the user to insert the payment. Once the it's
    # It then prints the change
    # The if statement and while
    # loop will print if the amount is less than the amount ask.
    # If it's less than the amount,
    #  it will prompt the user to pay the amount required
    """ TA Mr. Jairo helped me with an issue with my try and except for the 
    customer's payment. And also brought the insight on negative numbers 
    being involved. -_-
    """

    while True:
        try:
            costumer_payment = float(
                input("Please, pay the amount required. "))
            if costumer_payment > 0:
                break
            break
        except ValueError:
            print("Improper input. Input a whole or float number.")

    while costumer_payment < cost:
        print("Insufficient amount, please pay the required amount. ")
        try:
            costumer_payment = float(input("Please, "
                                           "pay the amount required."))
        except ValueError:
            print("Improper input. Input a whole or float number.")

    difference = costumer_payment - cost
    print("Your change is $", format(difference, '.2f'), sep='')

    # This part of the code will ask for tips and will verify a yes or no from
    # the customer's input
    # If yes it will go through the tip and verify the amount made.
    # will then print out the change along with the receipt.
    # if no it will print the receipt.
    tip = 0
    ask_for_tip = input("Would you like to tip us? Type Yes or No.: ")
    while ask_for_tip == "Yes" or ask_for_tip == "yes" or ask_for_tip == \
            "no" \
            or \
            ask_for_tip == "No":
        if ask_for_tip == "yes" or ask_for_tip == "Yes":
            while True:
                try:
                    tip = float(
                        input('Okay how much would you like to tip us?: '))
                    break
                except ValueError:
                    print("Improper input. Input a whole or float number.")
            if tip < 0:
                print("insufficient amount. Please provide a proper input.")
                try:
                    tip = float(input('Okay how much would '
                                      'you like to tip us?: '))
                    break
                except ValueError:
                    print("Improper input. Input a whole or float number.")
        elif ask_for_tip == "no" or "No":
            print("Thank you " * 2 + " for coming!" +
                  "\n Subscribe to our mail letter for our new dishes. \n")
            print("spunky", "joe", sep="", end="@")
            print("gmail.com \n")
            print("04", "20", "2021", sep="-", )
            break
        else:
            print("Please provide a proper input.")

    new_payment = difference - tip
    print("Your new change is $", format(new_payment, '.2f'), sep='')
    print("Thank you " * 2 +
          " for coming!" + "\n "
                           "Subscribe to our mail "
                           "letter for our new dishes. \n")
    print("spunky", "joe", sep="", end="@")
    print("gmail.com \n")
    print("04", "20", "2021", sep="-")


main()
