# Assignment 1: Design Your Own Class

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, and I protect {self.city}!")

    def save_the_day(self):
        print(f"{self.name} uses {self.power} to save {self.city}!")

# Inheritance layer
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

       
    def fly(self):
        print(f"{self.name} flies at {self.flight_speed} km/h!")

    # Polymorphism: override save_the_day
    def save_the_day(self):
        print(f"{self.name} swoops in at {self.flight_speed} km/h to save {self.city}!")

# Example usage
hero1 = Superhero("Shadow", "Invisibility", "Metro City")
hero2 = FlyingSuperhero("Skybolt", "Lightning", "Star City", 500)

hero1.introduce()
hero1.save_the_day()
hero2.introduce()
hero2.fly()
hero2.save_the_day()


print("\n--- Activity 2: Polymorphism Challenge ---\n")

# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()      
