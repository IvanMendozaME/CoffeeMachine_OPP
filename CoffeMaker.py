class CoffeMaker():
    def __init__(self):
        self.resources = {
            "water":300,
            "milk":200,
            "coffee":100,
            "money":0,
        }
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: $ {self.resources['money']}")
    def is_resource_sufficient(self,drink):
        can_make = True
        for i in drink.ingredients:
            if drink.ingredients[i] > self.resources[i]:
                print("Sorry, I have enough {i}")
                can_make = False
        return can_make
    def make_coffee(self, order, change):
        for i in order.ingredients:
            self.resources[i] -= order.ingredients[i]
        self.resources["money"] += change
        print(f"Here is your: {order.name}")
            