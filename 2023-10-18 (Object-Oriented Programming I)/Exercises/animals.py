class Dog:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __str__(self):
        return f"{self.name} ({self.mass} kg)"

    def __lt__(self, other):
        return self.mass < other.mass


dog = Dog("Fido", 10)
print(dog)  # Fido (10 kg)
print(dog.mass)  # 10
dog2 = Dog("Buddy", 20)
print(dog2)  # Buddy (20 kg)
print(dog2.mass)  # 20
print(dog < dog2)  # True
print(dog2 < dog)  # False
