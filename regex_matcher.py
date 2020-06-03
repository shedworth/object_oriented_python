import sys
import re

search_string = sys.argv[1]
pattern = sys.argv[2]
match = re.match(pattern, search_string)

print(f"'{search_string}' {'matches' if match else 'does not match'} pattern '{pattern}'")