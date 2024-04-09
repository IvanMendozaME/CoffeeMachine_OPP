class MoneyMachine():
    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    def __init__(self):
        self.profit = 0
        self.received = 0
    def report(self):
        print(f"Money: {self.CURRENCY} {self.profit}")


    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.received
    
    def make_payment(self,cost):
        Payment = True
        if self.received < cost:
            print(f"We can not continue with the purchase, the cost is{cost} and you are trying to pay with {self.received}")
            Payment = False
        elif self.received >= cost:
            change = round(self.received - cost,2)
            self.profit += cost
            self.received = 0
            print(f"Your change is: ${change} dollars")
        return Payment, change