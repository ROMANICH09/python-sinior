
import random
class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.money = 100
        self.happiness = 50
        self.hunger = 50
        self.food = 50
        self.car_fuel = 50
        self.house_mess = 0

    def eat(self):
        if self.food > 0:
            print(f"{self.name} is eating...")
            self.food -= 10
            self.hunger = min(100, self.hunger + 10)  # Hunger cannot exceed 100
        else:
            print(f"{self.name} has no food left! Maybe eat his cat...?")

    def work(self):
        print(f"{self.name} is working...")
        earnings = random.randint(30, 50)
        self.money += earnings
        self.happiness -= 5
        self.hunger -= 5
        self.car_fuel -= 10
        print(f"{self.name} earned {earnings} money.")

    def relax(self):
        print(f"{self.name} is relaxing...")
        self.happiness = min(100, self.happiness + 10)  # Happiness cannot exceed 100
        self.house_mess += 5

    def clean(self):
        print(f"{self.name} is cleaning...")
        self.house_mess = 0
        self.happiness -= 5

    def shop(self, item):
        if item == "food":
            print(f"{self.name} bought some food!")
            self.money -= 30
            self.food += 30
        elif item == "fuel":
            print(f"{self.name} bought car fuel!")
            self.money -= 50
            self.car_fuel += 50

    def girlfriend(self):
        """Simulates girlfriend interactions."""
        outcomes = ["nothing", "new_iphone", "argue", "clean_mess"]
        action = random.choice(outcomes)

        if action == "nothing":
            print("Your girlfriend is in a good mood and does nothing.")
        elif action == "new_iphone":
            spent_money = self.money // 2
            self.money -= spent_money
            print(f"Your girlfriend bought a new iPhone and took {spent_money} money!")
        elif action == "argue":
            lost_happiness = self.happiness // 2
            self.happiness -= lost_happiness
            print(f"You had an argument! Your happiness decreased by {lost_happiness}.")
        elif action == "clean_mess":
            print("Your girlfriend is feeling generous and cleaned all the mess in the house!")
            self.house_mess = 0

    def status(self, day):
        print(f"\nDay {day}. {self.name}'s life:")
        print(f"Money: {self.money}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        print(f"Food at home: {self.food}, Car fuel: {self.car_fuel}, House mess: {self.house_mess}")

    def live(self, day):
        self.status(day)

        # Girlfriend interaction
        self.girlfriend()

        if self.hunger < 20:
            self.eat()
        elif self.car_fuel < 20:
            self.shop("fuel")
        elif self.money < 0:
            self.work()
        elif self.house_mess > 20:
            self.clean()
        else:
            action = random.choice(["work", "relax", "shop"])
            if action == "work":
                self.work()
            elif action == "relax":
                self.relax()
            elif action == "shop":
                self.shop("food")

        if self.happiness <= 0 or self.hunger <= 0 or self.money < -100:
            print(f"{self.name} couldn't go on living...")
            return False
        return True


# Simulation
roman = Human(name="Roman")

for day in range(1, 150):
    if not roman.live(day):
        break
