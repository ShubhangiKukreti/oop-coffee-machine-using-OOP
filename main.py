from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
drinks = menu.get_items()

coffee = CoffeeMaker()
money = MoneyMachine()

while True:
    user_input = input(print(f"What do you want to drink? {drinks}"))

    if user_input == "report":
        coffee.report()
        money.report()
    elif user_input == "off":
        exit()
    else:
        user_choice = menu.find_drink(user_input)
        if coffee.is_resource_sufficient(user_choice) and money.make_payment(user_choice.cost):
            coffee.make_coffee(user_choice)


