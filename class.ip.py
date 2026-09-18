"""
CLASS deep diving
(1) Encapsulation
(2) Inheritance 
(3) Polimorphism 
"""

print(" ==== Inheritance ====")
# PARENT > CHILD( properties > state, method)
# Parent inherits only public & protected property(state + method) to children!

class Animal:  # Parent
    # state
    description = "The class creates animals"
    # constructor

    def __init__(self, voice):
        self.message = "Animal is alive"
        self.voice = voice

        # method
    def make_voice(self):
        print(f"the animal make voice:  {self.voice}")


class Dog(Animal):  # Child
    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):  # Child
    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        print("Yes, I can give you a calmy therapy!")


class Fish(Animal):  # Child

    # state
    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can teach you how to swim!")
        print(Animal.description)


dog = Dog("Rex", "Wow", True)
cat = Cat("Tom", "Meow", True)
fish = Cat("Nemo", "Zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("=============")
dog.make_voice()
fish.make_voice()

print(" --------")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print(dog.message, fish.message)
