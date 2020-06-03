"""Decorator"""
def insult(func):
    def wrapper(*args, **kwargs):
        print("The answer is...")
        func(*args, **kwargs)
        print("...you tosser!")
    return wrapper

def validate(func):
    def wrapper(*args, **kwargs):
        if "password" in kwargs:
            if kwargs['password'] == "walrus":
                return func(*args)
        print("password incorrect")
    return wrapper

class InsultMath:

    def insultiply(self, *args, **kwargs):

        @validate
        @insult
        def multiply(*args, **kwargs):
            result = args[0]
            for arg in args[1:]:
                result = result * arg 
            print(result)

        multiply(*args, **kwargs)


    def insultadd(self, *args, **kwargs):

        @validate
        @insult
        def add(*args, **kwargs):
            result = args[0]
            for arg in args[1:]:
                result = result + arg
            print(result)

        add(*args, **kwargs)


    def insultsubtract(self, *args):

        @insult
        def subtract(*args):
            result = args[0]
            for arg in args[1:]:
                result = result - arg
            print(result)

        subtract(*args)


    def insultdivide(self, *args):

        @insult
        def divide(*args):
            result = args[0]
            for arg in args[1:]:
                result = result / arg
            if result % 1 == 0:
                result = int(result)
            print(result)

        divide(*args)
