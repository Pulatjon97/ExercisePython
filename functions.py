'''
FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope 
'''

print("==== DEFINE (parametr) vs CALL (argument)====")
# builtin functions > print() type()
# Functions - reusable block of code!
# Inside of block {} in Java, Python uses indentation!

# DEFINE - parametr


def greet(a):
    print(f"How do you do, {a}" + "?")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


    # CALL - argument
result1 = greet('John')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)

print("==== Keyword & default arguments ====")
# DEFINE


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


result3 = give_greet(name="John", age=28)
print("result3:", result3)

result4 = give_greet("Justin")
print("result4:", result4)


print("==== SCOPE ====")
b = 100  # 3


# DEFINE
def calculate(a, b):  # 2
    c = a * b  # 1
    print(f"the c value: {c}")


# CALL
calculate(5, 50)
