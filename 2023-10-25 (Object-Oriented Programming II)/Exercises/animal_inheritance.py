class Pet:
    def __init__(self, name, breed, mass, sex):
        self._name = name
        self._breed = breed
        self._mass = mass
        self._sex = sex


class Dog(Pet):
    def speak(self):
        print(f"{self._name}: Woof!")


class Cat(Pet):
    def speak(self):
        print(f"{self._name}: Meow!")


pets = [Dog("Rufus", "Husky", 8.0, "female"), Cat("Boots", "Long hair", 3.2, "male")]
for pet in pets:
    pet.speak()
