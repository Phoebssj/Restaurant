#Sheryll Jacquet
#An integration porject on what I've learn so far, In a Restaurant Demographic.
#The first part represents my understanding with format, inputs and vairables.

#The first string will greet the customer and introduce them to the restaurant.
#It then prints out the menu.
def calculate_total(total1, total2, total3):
    total = (total1 + total2 + total3)+(59%6)/100
    return total
def WelcomeCustomer():
  """
  This function can be called each and everytime we have to refer to the 
  current customer.
  """
  customer_name = input("Enter your name: ")
  return customer_name

customer = WelcomeCustomer()
print("Welcome " + customer + " to Spunky Joe's Quesine Restaurant! \n Here is the Menu for tonight!:")

full_menu = open('FullMenu.txt')
for x in range(23):
    fm = full_menu.readline()
    print(fm)

"""These variables represent the appetizers section of the menu and 
their their prices. appet_ are the name of the dishes and appet_#_price are
their cost."""
appet_1 = "Garlic Bread Crumpets"
appet_1_price = 4.49

appet_2 = "Caeser Salad with Dressing"
appet_2_price = 5.50

appet_3 = "Chips with Jalepeño Dip"
appet_3_price = 3.49

#These are variables to represent the main dish section of the menu.\n
#main_dish represents the names of each dish and main_dish_#_price are there prices.
main_dish_1 = "Filet Mignon"
main_dish_1_price = 15.49

main_dish_2 = "Fruit Salad with Grilled Fish"
main_dish_2_price = 13.50

main_dish_3 = "Garlic Alfredo with Shrimp, Peppers & Onions"
main_dish_3_price = 14.49

#These are variables to represent the beverage section of the menu.\n
#bev_ represents the names of each drink and bev_#_price are there prices.
bev_1 = "Apple Cider"
bev_1_price = 5.00

bev_2 = "Sparkling Water"
bev_2_price = 2.50

bev_3 = "Grape Wine"
bev_3_price = 6.49

def main():
    #These lines of code give an opiton for customers to decline or
    #Decide for having a snack before their main dish.
    ask_for_appetizer = input(f"Would you like an appetizer. Type Yes or No.: ")
    if ask_for_appetizer == "yes" or ask_for_appetizer == "Yes":
      appetizer_menu = open('Appetizer.txt')
      for x in range(6):
        am = appetizer_menu.readline()
        print(am) # If yes a section of the menu will be printed for them
      appet = input("What appetizer would you like?: ")
      appet_qt = input("How many would you like?: ")
      return [appet, appet_qt] # Since we can't get the inputs from user my uncle
      #suggested to use a list instead that way we can call their value
    elif ask_for_appetizer == "no" or ask_for_appetizer == "No":
        print("Okay let's move on to the next selection")
        return None
        #That's where the main dish menu will be printed.
    else:
        ("Sorry " + ask_for_appetizer + "\n Is not a proper input.\n" + "Please provide a proper input")
        return main()# This option loops back in order to get a proper answer.
      
#Another issue we ran into was making sure the variables existed.
#So we used an if statement to verify if the appetizer options are mentioned
#that way it's represented as new variables. If not it will be ignored and 
#will move on to the next section

appet_list = main()
if appet_list:
  for i in range(len(appet_list)):
    appet_chosen = appet_list[0]
    appet_chosen_qt = int(appet_list[1])

""" This code opens the text file for the main dish"""
main_menu = open('mainmenu.txt')
for x in range(6):
    mm = main_menu.readline()
    print(mm)

main_dish = input("Main dish of choice?: ")

main_dish_qt = int(input("How many servings would you like?: "))
""" This code opens the text file for Beverages"""
beverage_menu = open('Beverage.txt')
for x in range(8):
    bm = beverage_menu.readline()
    print(bm)

bev = input("Beverage of Choice?: ")

bev_qt = int(input("How many serving would you like?: "))


#Find out which appetizer the customer chose and what's the total price.
#Recalling from the previous list this will verify if the list exist. if it does
#we can call the option of the appetizer and it qt in order to to calculet the 
#total price of the appetizer. If not it will skip the calucations for appetizers
#and move on to the main dish calculations.

appet_total = 0
if appet_list:
  if appet_chosen == appet_1:
    appet_price_total = appet_1_price * appet_chosen_qt
    print(f'You purchased {appet_chosen_qt} {appet_1} for ${appet_price_total}.')
  elif appet_chosen == appet_2:
    appet_price_total = appet_2_price * appet_chosen_qt
    print(f'You purchased {appet_chosen_qt} {appet_2} for ${appet_price_total}.')
  elif appet_chosen == appet_3:
    appet_price_total = appet_3_price * appet_chosen_qt
    print(f'You purchased {appet_chosen_qt} {appet_3} for ${appet_price_total}.')
  else:
   print("We don't have the appetizer that you mentionned, look back at the menu.")

#Find out which main dish the customer chose and what's the price.
main_dish_total = 0

if main_dish == main_dish_1:
  main_dish_total = main_dish_1_price * main_dish_qt
  print(f'You purchased {main_dish_qt} {main_dish_1} for ${main_dish_total}')
elif main_dish == main_dish_2:
  main_dish_total = main_dish_2_price * main_dish_qt
  print(f'You purchased {main_dish_qt} {main_dish_2} for ${main_dish_total}')
elif main_dish == main_dish_3:
  main_dish_total = main_dish_3_price * main_dish_qt
  print(f'You purchased {main_dish_qt} {main_dish_3} for ${main_dish_total}')
else:
  print("we don't have the main dish that you mentionned, look back at the menu.")

#Find out which beverage the customer chose and what's the price.
bev_total = 0

if bev == bev_1:
  bev_total = bev_1_price * bev_qt
  print(f"You purchased {bev_qt} {bev_1} for ${bev_total}.")
elif bev == bev_2:
  bev_total = bev_2_price * bev_qt
  print(f"You purchased {bev_qt} {bev_2} for ${bev_total}.")
elif bev == bev_3:
  bev_total = bev_3_price * bev_qt
  print(f"You purchased {bev_qt} {bev_3} for ${bev_total}.")
else:
  print("we don't have the beverage that you mentionned, look back at the menu.")

#Find out the total we should charge the costumer. As it's calculated by the 
#function.
total = calculate_total(appet_total, main_dish_total, bev_total)
print("Your total cost for this dinner is $",format(total,'.2f'), sep='')
#This input allows the user to insert the payment. Once the it's
# It then prints the change 
# The if statement and while
# loop will print if the amount is less than the amount ask.
#If it's less than the amount it will prompt the user to pay the amount required


costumer_payment = float(input("Please, pay the amount required."))
while not costumer_payment  == total:
      if costumer_payment == total or costumer_payment >= total:
        difference = costumer_payment - total
        print("Your change is $",format(difference,'.2f'), sep='')
        break
      else:
        print("Insuficient ammount, please pay the required amount. ")
        costumer_payment = float(input("Please, pay the amount required. "))

ask_for_tip = input(f"Would you like to tip us? Type Yes or No.: ")
if ask_for_tip == "yes" or ask_for_tip == "Yes":
  tip = int(input(f" Okay how much would you like to tip us?: "))
  difference-=tip
  print("Your new change is $",format(difference,'.2f'), sep='')
  print("Thank you "*2 + " for coming!" + 
  "\n Subscribe to our mail letter for our new dishes. \n")
  print("spunky", "joe", sep="", end="@")
  print("gmail.com \n")
  print("04", "20", "2021", sep="-", end="\n")
else:
  print("Thank you "*2 + " for coming!" + 
  "\n Subscribe to our mail letter for our new dishes. \n")
  print("spunky", "joe", sep="", end="@")
  print("gmail.com \n")
  print("04", "20", "2021", sep="-", end="\n")
