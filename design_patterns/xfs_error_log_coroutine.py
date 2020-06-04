"""
Searches log file for hard drives reporting errors and prints their
serial numbers:
    1. Find error message
    2. Get device name corresponding to error message
    3. Get bus name corresponding to device name
    4. Get serial number corresponding to bus name
"""

import re
import types
"""Coroutine that reads file in reverse and yields first 
matching instance of regex"""
@types.coroutine
def match_regex(filename, regex):
    with open(filename) as file:
        lines = file.readlines()
    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            """regexes sent to function get injected on this line.
            Matches also yielded on this line"""
            regex = yield match.groups()[0]


"""Function that manages a matcher coroutine and tells it what
to match next"""
def get_serials(filename):
    ERROR_RE = "XFS ERROR (\[sd[a-z]\])"
    matcher = match_regex(filename, ERROR_RE)
    """Store name of first device showing an error"""
    device = next(matcher)
    while True:
        try:
            """Find bus corresponding to device"""
            bus = matcher.send(
                "(sd \S+) {}*".format(re.escape(device))
            )
            """Find serial corresponding to bus"""
            serial = matcher.send("{} \(SERIAL=([^)]*)\)".format(bus))
            """Return serial number and wait for 'next' call"""
            yield serial
            """Store name of next device showing an error"""
            device = matcher.send(ERROR_RE)
        except StopIteration:
            matcher.close()
            return


for serial_number in get_serials("example_log.log"):
    print(serial_number)