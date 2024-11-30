import random

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 50  # Голод (0-100)
        self.energy = 50  # Энергия (0-100)
        self.happiness = 50  # Счастье (0-100)

    def feed(self):
        """Покормить котика"""
        self.hunger = max(0, self.hunger - 30)  # Уменьшаем голод больше
        self.happiness = min(100, self.happiness + 10)
        print(f"{self.name} покушал. Голод: {self.hunger}, Счастье: {self.happiness}")

    def play(self):
        """Поиграть с котиком"""
        if self.age >= 15:
            print(f"{self.name} уже не играет, он слишком взрослый для игр.")
        elif self.energy >= 20:
            self.happiness = min(100, self.happiness + 20)
            self.energy -= 20  # Игра снижает энергию
            self.hunger = min(100, self.hunger + 10)  # После игр котик становится голоднее
            print(f"{self.name} поиграл. Счастье: {self.happiness}, Энергия: {self.energy}, Голод: {self.hunger}")
        else:
            print(f"{self.name} слишком устал, чтобы играть!")

    def rest(self):
        """Дать котику отдохнуть"""
        self.energy = min(100, self.energy + 50)  # Восстанавливаем энергию больше
        self.hunger = min(100, self.hunger + 10)  # После отдыха котик проголодается
        print(f"{self.name} отдохнул. Энергия: {self.energy}, Голод: {self.hunger}")

    def random_event(self):
        """Случайное событие дня"""
        event = random.choice(["плохая погода", "хорошая погода", "гости", "ничего особенного"])
        if event == "плохая погода":
            self.happiness = max(0, self.happiness - 10)
            print(f"{self.name} грустит из-за плохой погоды.")
        elif event == "хорошая погода":
            self.happiness = min(100, self.happiness + 10)
            print(f"{self.name} радуется хорошей погоде!")
        elif event == "гости":
            self.happiness = min(100, self.happiness + 20)
            self.energy = max(0, self.energy - 15)
            print(f"К {self.name} пришли гости. Он доволен, но устал.")
        else:
            print(f"У {self.name} спокойный день, ничего особенного.")

    def status(self):
        """Показать состояние котика"""
        print(f"Котик: {self.name}, Возраст: {self.age}")
        print(f"Голод: {self.hunger}, Энергия: {self.energy}, Счастье: {self.happiness}")

    def live_a_day(self):
        """Симуляция одного дня жизни котика"""
        print(f"День из жизни {self.name}")

        # Каждый день котик немного проголодается и устанет
        self.hunger = min(100, self.hunger + 15)
        self.energy = max(0, self.energy - 10)

        self.random_event()  # Случайное событие дня

        if self.hunger > 70:
            print(f"{self.name} голоден. Надо покормить!")
            self.feed()
        elif self.happiness < 40:
            print(f"{self.name} скучает. Надо поиграть!")
            self.play()
        elif self.energy < 30:
            print(f"{self.name} устал. Надо дать ему отдохнуть.")
            self.rest()
        else:
            print(f"{self.name} чувствует себя хорошо. Можно просто любоваться им!")

        self.status()
        print("-" * 30)

# Пример использования
mishka = Cat("Мишка", 15)  # Создаём котика по имени Мишка с возрастом 15 лет
for _ in range(5):  # Проживём 5 дней с Мишкой
    mishka.live_a_day()
