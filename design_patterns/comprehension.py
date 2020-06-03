"""General format:
output_list = [func(iterator) for iterator in iterable if filter == True]"""


"""List comprehension"""
input_list = ["1", "72", "343", "54", "4556"]

output_list = [int(str) for str in input_list if len(str) < 3]

print(output_list)

# prints [1, 72, 54]


"""Set comprehension"""
from collections import namedtuple
Book = namedtuple("Book", "author title genre")
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief of Time", "fantasy"),
    Book("Pullman", "The Amber Spyglass", "fantasy"),
    Book("Ian Banks", "The Wasp Factory", "horror"),
    Book("Walsh", "Trainspotting", "dark comedy"),
]

fantasy_authors = {b.author for b in books if b.genre == "fantasy"}

print(fantasy_authors)

# prints {"Pullman", "Pratchett"}


"""Dictionary comprehension"""
fantasy_titles = {b.title: b for b in books if b.genre == "fantasy"}

print(fantasy_titles)

"""prints
{
    'Nightwatch': 
        Book(author='Pratchett', title='Nightwatch', genre='fantasy'),
    'Thief of Time':
        Book(author='Pratchett', title='Thief of Time', genre='fantasy'),
    'The Amber Spyglass':
        Book(author='Pullman', title='The Amber Spyglass', genre='fantasy')
}
"""