"""
(1) What is class
(2) Ordinary vs static properties
(3) Special Methods
"""
print("===== What is class =====")
# class - blueprint for object creation!
# structure > state constuctor method

class Person:
    # state
    message = "static state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: Hello, How do you do!?")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        print("Class: static method properties executed")


person1 = Person("John", 28)
person2 = Person("Martin", 30)
person3 = Person("Justin", 32)

# ordinary state property
name = person1.name
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person1.say_age()


print("===== Ordinary vs static properties =====")
new_message = Person.message
print("new_message:", new_message)

# static state
Person.explain()


print("===== Special/Magic Methods =====")
# Python's most common special methods are below:
# __init__  __new__ __str__ __call__ __getitem__ __eq__ __len ...

class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, name, year):
        print("*__new*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"the  {self.name} started engine!")

    def stop_engine(self):
        print(f"the  {self.name} stopped engine!")

    def __str__(self):
        return f"the car nar.name: {self.name} was produced in {self.year} year!"

    def __call__(self):
        print("Object called as function!")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("-----------")
your_car = Car("Toyota", 2026)
print(your_car)
print(your_car) 
response = your_car() # CALL
print("response:", response)

# print(dir(__builtins__))
