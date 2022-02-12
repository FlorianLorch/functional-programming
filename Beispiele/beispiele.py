import logging
logger = logging.Logger

# First-Class Functions

def myFunc(string):
    print("Run myFunc(): ", string)
    
x = myFunc

x("Hello World")


# Functions Higher Order

def outerFunc(innerFunc):
    print("Running inner function")
    innerFunc()
    print("Done with inner function")

def myInnerFunc():
    print("Doing Stuff...")

outerFunc(myInnerFunc)

# Map

def output_text(count, message, function):
    for i in range(count):
        function(message)

output_text(5, "Hello World", print)

map(print, "hi")

# Currying 

def multiplizieren(a, b):
    return a * b

def konstruktor(func, num):
    return lambda y: func(num, y)

verdoppeln = konstruktor(multiplizieren, 2)

verdreifachen = konstruktor(multiplizieren, 3)

print(verdoppeln(5))

print(verdreifachen(5))

