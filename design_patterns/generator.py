"""Generators differ from list comprehensions, in that they do
not create a final container object, i.e a list, set or 
dictionary. Instead, they iterate through an iterable and 
instantly return their values. Generators consume far less
memory space than comprehensions, and are invaluable when dealing
with very large iterables (e.g. a log file with millions of
lines of code. This example shows a program for iterating through
a log file and writing any warning messages into another file."""

"""Generator expression written using list-comprehension-style
syntax with round brackets () """
infile = ""
warnings = (line for line in infile if 'WARNING' in line)


"""More complete generator example, showing the special 'yield'
function"""

"""Generator function"""
def warnings_filter(insequence):
    for l in insequence:
        if "WARNING" in l:
            """'yield' returns a value but pauses
            the iteration at its current position, 
            ready to pick up again when called again
            by '__next__'"""
            yield l.replace("\tWARNING", "")


"""Outer function that takes in a logfile, uses the
generator to find all 'warning' messages, and writes 
them to a different file"""
def filter_logs(inname, outname):
    with open(inname) as infile:
        with open(outname, "w") as outfile:
            filter = warnings_filter(infile)
            for l in filter:
                outfile.write(l)
