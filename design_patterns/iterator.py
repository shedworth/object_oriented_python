"""Verbose illustration of Python's __iter__ and __next__ methods,
used to handle iteration, usually hidden 'under the hood'"""

"""An 'iterable' is an object that can be looped over"""
"""An 'iterator' is a specific location within an iterator""" 


"""__iter__ method satisfies the Iterable interface defined in
collections.abc.Iterable, therefore
issubclass(CapitalIterable, collections.abc.Iterable) == True""" 
class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)




"""__iter__ method satisfies the Iterable interface defined in
collections.abc.Iterable, therefore
issubclass(CapitalIterator, collections.abc.Iterable) == True""" 

"""__next__ and __iter__ methods satisfy the Iterator interface 
defined in collections.abc.Iterator, therefore
issubclass(CapitalIterator, collections.abc.Iterator) == True""" 
class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self



iterable = CapitalIterable(
    'the quick brown fox jumps over the lazy dog'
    )
iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
"""
Returns...
The
Quick
Brown 
Fox 
Jumps 
Over 
The 
Lazy 
Dog 
"""