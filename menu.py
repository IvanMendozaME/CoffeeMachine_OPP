class MenuItem():
    def __init__(self,name,water,milk,coffee,cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water":water,
            "milk":milk,
            "coffee":coffee
        }

class Menu():
    def __init__(self):
        self.menu = [
            MenuItem(name="latte",water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso",water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino",water=250, milk=50, coffee=24, cost=3),
        ]
    def get_items(self):
        options = ""
        for i in self.menu:
            options += f"{i.name}/"
        return options
    def find_drink(self, order_name):
        for i in self.menu:
            if i.name == order_name:
                return i.name
            else:
                print("Sorry, that item does not exist")
                return "False"
