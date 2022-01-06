nums = [1, 2, 3]
letters = ["A", "B", "C"]

zipped = zip(nums, letters) # zip object created i.e an iterable

print(next(zipped)) # (1, 'A')

# the number of elements that zip() returns will be equal
# to the length of the shortest iterable
list(zip(range(5), range(100))) # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

longest = range(5)

# Avoid this by using itertools.zip_longest()
from itertools import zip_longest
longest = range(5)
zipped = zip_longest(nums, letters, longest, fillvalue='?')

# [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]

