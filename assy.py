# Question 1
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name}, from {self.origin}, and I can {self.power}!")

    def attack(self):
        print(f"{self.name} uses {self.power}!")

# Subclass with inheritance and polymorphism
class Titan(Superhero):
    def __init__(self, origin, strength_level):
        super().__init__("Titan", "super strength", origin)
        self.strength_level = strength_level

    def attack(self):
        print(f"{self.name} smashes with strength level {self.strength_level}!")

# Another subclass
class Telepath(Superhero):
    def __init__(self, name, origin, mind_control_level):
        super().__init__(name, "mind control", origin)
        self.mind_control_level = mind_control_level

    def attack(self):
        print(f"{self.name} uses mind control at level {self.mind_control_level}!")

# Creating objects
hero1 = Titan("Mars-7", 9000)
hero2 = Telepath("MindWave", "Nebula-5", "Ultra")

hero1.introduce()
hero1.attack()

hero2.introduce()
hero2.attack()

# Question 2

class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚤")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
