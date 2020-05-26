"""Decorator"""
def insult(func):
    def wrapper(*args, **kwargs):
        print("The answer is...")
        func(*args, **kwargs)
        print("...you tosser!")
    return wrapper


class InsultMath:

    def insultiply(self, *args):

        @insult
        def multiply(*args):
            result = args[0]
            for arg in args[1:]:
                result = result * arg 
            print(result)

        multiply(*args)


    def insultadd(self, *args):

        @insult
        def add(*args):
            result = args[0]
            for arg in args[1:]:
                result = result + arg
            print(result)

        add(*args)


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
