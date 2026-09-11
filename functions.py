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
