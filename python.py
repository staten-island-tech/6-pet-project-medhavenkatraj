class pet:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    pet_name = input("HI, you were recently gifted a new pet dog! pick a name for it! ")
    print("what a wonderful name!")
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

