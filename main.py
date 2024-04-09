from menu import Menu, MenuItem
from CoffeMaker import CoffeMaker
from MoneyMachine import MoneyMachine


CoffeMake = CoffeMaker()
Menu2 = Menu()
Money_Machine = MoneyMachine()

select = "on"
while select != "off":
    select = input(f"What would you like? ? ({Menu2.get_items()}) ")
    if select == "report":
        CoffeMake.report()
    else:
        Drink = Menu2.find_drink(select)
        if Drink != "False":
             for i in Menu2.menu:
                 if i.name == Drink:
                     PropertiesDrink = i

             CanMake = CoffeMake.is_resource_sufficient(PropertiesDrink)
             if CanMake == True:
                MoneyReceived =  Money_Machine.process_coins()
                Payment, change = Money_Machine.make_payment(PropertiesDrink.cost)
                if Payment == True:
                    CoffeMake.make_coffee(PropertiesDrink, change)

print("Maintainence mode")
