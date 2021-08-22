## ********Day 54 Start**********
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
# inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)
# decorated_function = delay_decorator(say_hello)
#decorated_function()

# say_hello()
# say_bye()

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(funct):
    def wrapper(*args):
#        if user.is_logged_in == True:
        if args[0].is_logged_in == True:
            funct(args[0])
    return wrapper

def logging_decorator(funct):
    def wrapper(*args, **kwargs):
        print('\n\nfunct name: ', funct.__name__)
        for arg in kwargs:
            print('kwarg: ', arg)
        funct(args, kwargs)
    return wrapper

def create_blos_post(user):
#    print('self: ', __name__)
    print(f"this is {user.name}'s new blog post.")

@logging_decorator
def hello_log(args, kargs):
    print("args:", args, ", kargs: ", kargs)

new_user = User("pac")
new_user.is_logged_in = True
# create_blos_post(new_user)
# theList = ["abc", "def"]
hello_log(a="alpha", b="beta", c="gamma"  )
