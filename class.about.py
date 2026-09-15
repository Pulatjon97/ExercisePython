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