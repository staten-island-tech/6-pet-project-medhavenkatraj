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



""" def __init__(self, name, money, happiness):
        self.name = name
        self.money = money
        self.happiness = happiness
class pet:
    def pet:
    name = []
    pet_name = input("HI, you were recently gifted a new pet dog! pick a name for it! ").lower()
    name.append(pet_name)
    print(name,"what a wonderful name!")
    answer = input(name, "is on 100 health. would you like to have ur pet take a nap ")
    while True:
        print(name, "is well rested and is at 110 health!") """


class pet():
    def __init__(self, name, play = 5, happiness = 10, sleep = 5, energy = 10, eat = 5 ):
        self.name = name
        self.play = play
        self.happiness = happiness
        self.sleep = sleep
        self.energy = energy
        self.eat = eat

def new_pet():
    pet_name = input("HI, you were recently gifted a new pet dog! pick a name for it! ")
    my_pet = pet(pet_name)
    print(pet_name,"is such a wonderful name!")
    while True:
        answer = input(f"{pet_name} ... would you like to play, sleep, eat, analyze stats, or quit. ")
        if answer == "play":
            my_pet.energy -=5
            my_pet.happiness +=5
            print(pet_name, "is excited to play!")
            print("-5 energy, +5 happiness")
            print("ur pet is getting hungry... eat to raise their energy...or else")
        elif answer == "sleep":
            my_pet.energy +=5
            my_pet.happiness +=5
            print("+5 energy, +5 happiness")
            print(pet_name, "was so sleepyyy")
            print("ur pet is well rested! this is the amount of health ur pet is at now. ur pet is eager to playyy")
        elif answer == "eat":
            my_pet.energy +=5
            my_pet.happiness -=5
            print("ur pet is full! yum! ")
            print("+5 energy, -5 happiness")
        elif answer == "analyze":
            print(pet_name, "has", str(my_pet.energy), "energy and", str(my_pet.happiness), "happiness")
            if my_pet.energy <= 0:
                print(pet_name, "has died...")
            if my_pet.happiness <= 0:
                print(pet_name, "has died...")
        elif answer == "quit":
            print("bye! that was so fun! come again soon! ")
            break
        else:
            print("invalid answer, try again ")
            continue
          

new_pet()