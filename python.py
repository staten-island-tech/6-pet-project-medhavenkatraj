""" class pet:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    pet_name = input("HI, you were recently gifted a new pet dog! pick a name for it! ")
    print("what a wonderful name!")
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
 """

class pet:
    def __init__(self, name, money, happiness):
        self.name = name
        self.money = money
        self.happiness = happiness
    name = []
    pet_name = input("HI, you were recently gifted a new pet dog! pick a name for it! ").lower()
    name.append(pet_name)
    print(name,"what a wonderful name!")
    answer = input(name, "is on 100 health. would you like to have ur pet take a nap ")
    while True:
        print(name, "is well rested and is at 110 health!")