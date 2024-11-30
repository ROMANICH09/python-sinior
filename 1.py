class Student:
    def __init__(self, name, lastname, age, money=0):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.money = money
        self.grades = 70  # Успеваемость (0-100)
        self.energy = 50  # Энергия (0-100)

    def show_info(self):
        print(f"Имя: {self.name} {self.lastname}, Возраст: {self.age}")
        print(f"Деньги: {self.money}, Успеваемость: {self.grades}, Энергия: {self.energy}")

    def work(self):
        if self.energy >= 20:
            self.money += 50
            self.energy -= 20
            print(f"{self.name} поработал. Деньги: {self.money}, Энергия: {self.energy}")
        else:
            print(f"{self.name} слишком устал, чтобы работать!")

    def study(self):
        if self.energy >= 10:
            self.grades = min(100, self.grades + 10)
            self.energy -= 10
            print(f"{self.name} позанимался. Успеваемость: {self.grades}, Энергия: {self.energy}")
        else:
            print(f"{self.name} слишком устал, чтобы учиться!")

    def rest(self):
        self.energy = min(100, self.energy + 30)
        print(f"{self.name} отдохнул. Энергия: {self.energy}")

    def live_a_year(self):
        for day in range(1, 366):
            print(f"День {day}")
            if self.money < 20:
                print("Нехватка денег! Надо работать.")
                self.work()
            elif self.grades < 50:
                print("Успеваемость низкая! Надо учиться.")
                self.study()
            else:
                if self.energy < 30:
                    print("Усталость накопилась. Надо отдохнуть.")
                    self.rest()
                else:
                    print("Всё хорошо. Можно немного поработать.")
                    self.work()
            self.show_info()
            print("-" * 30)

# Пример использования:
s = Student("Roman", "Xenofontov", 15)
s.live_a_year()
