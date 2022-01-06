# Ref: https://realpython.com/python-strings/

### String methods ###

# replace()

# Replace all empty spaces in a string with "-" char

def replace_empty_chars(string):
    new_string = string.replace(" ", "-")
    return new_string

# capitalize()

# Returns a copy of s with the first character converted
# to uppercase and all other characters converted to lowercase

s = 'foO BaR BAZ quX'
s.capitalize() # 'Foo bar baz qux'

# lower()
s = 'FOO BAR BAZ'
s.lower()

# upper()
s = 'foo bar baz'
s.upper()

# swapcase()
'FOO Bar 123 baz qUX'.swapcase()

# title()
'the sun also rises'.title()

# count()
'foo goo moo'.count('oo') # 3

# Limited to <start> and <end>, if they are specified:
'foo goo moo'.count('oo', 0, 8) # 2

# endswith()
'foobarbaz'.endswith('baz')

# find()
'foo goo moo'.find('goo') # Returns lowest index e.g. 4 or -1

# index()
'foo goo moo'.index('zoo') # Identical to find() but raises ValueError exception

# rfind()
'foo bar foo baz foo qux'.rfind('foo') # Returns highest index e.g. 16

# rindex()
'foo bar foo baz foo qux'.rindex('zoo') # Identical to rfind() but raises ValueError exception

# startswith()
'foobar'.startswith('foo') # True

# isalnum()
'abc123'.isalnum() # All characters are alphanumeric

# isalpha()
'ABCabc'.isalpha() # All characters are alphabetic

# isdigit()
'123'.isdigit() # String is composed of only digits

# isidentifier()
'ABC_123'.isidentifier() # Only contains alphanumeric letters (a-z) and (0-9),
                         # or underscores (_). 
                         # A valid identifier cannot start with a number,
                         # or contain any spaces.

# islower()
'abc'.islower() # True

# isprintable()
'a\tb'.isprintable() # All the alphabetic characters it contains are printable

# isspace()
' \t \n '.isspace() # All characters are whitespace characters, this includes:
                    # \t
                    # \n
                    # ''


# istitle()
# Uppercase characters may only follow
# uncased characters and lowercase characters only cased ones
'This Is A Title'.istitle() # True
'This is a title'.istitle() # False
'Give Me The #$#@ Ball!'.istitle() # True

# isupper()
'ABC'.isupper() # True
'ABC1$D'.isupper() # True
'Abc1$D'.isupper() # False

# center()
# returns a string consisting of
# s centered in a field of width <width>.
# By default, padding consists of the ASCII space character
'foo'.center(10) # '   foo    '
'bar'.center(10, '-') # '---bar----'

# expandtabs()
# Expands tabs with spaces. Assumes tab stop at every eigth column
'a\tb\tc'.expandtabs() # 'a       b       c'
'aaa\tbbb\tc'.expandtabs(tabsize=4) # 'aaa bbb c'

# ljust()
'foo'.ljust(10) # 'foo       '
'foo'.ljust(10, '-') # 'foo-------'

# lstrip()
# Strip whitespace from left end
'   foo bar baz   '.lstrip() # 'foo bar baz   '

# Specify the set of characters to be removed:
'http://www.realpython.com'.lstrip('/:pth') # 'www.realpython.com'


# rjust()
'foo'.rjust(10) # '       foo'
'foo'.rjust(10, '-') # '-------foo'

# rstrip()
'   foo bar baz   '.rstrip() # '   foo bar baz'

# Specify the set of characters to be removed:
'foo.$$$;'.rstrip(';$.') # 'foo'

# strip()
# Strip whitespace from left and right ends
'    foo    '.strip() # 'foo'

# Specify the set of characters to be removed:
'www.realpython.com'.strip('w.moc') # 'realpython'

# zfill()
# Pads a string on the left with zeros to a total width
'42'.zfill(5) # '00042'
'+42'.zfill(8) # '+0000042'
'-42'.zfill(8) # '-0000042'

# join()
', '.join(['foo', 'bar', 'baz', 'qux']) # 'foo, bar, baz, qux'
list('corge') # ['c', 'o', 'r', 'g', 'e']
':'.join('corge') #'c:o:r:g:e'
'---'.join(['foo', str(23), 'bar']) # 'foo---23---bar'

# partition()
# s.partition(<sep>) splits s at the first occurrence of string <sep>.
# The return value is a three-part tuple consisting of:

 # The portion of s preceding <sep>
 # <sep> itself
 # The portion of s following <sep>

'foo.bar'.partition('.') # ('foo', '.', 'bar')
'foo@@bar@@baz'.partition('@@') # ('foo', '@@', 'bar@@baz')

# <sep> not found in string?
'foo.bar'.partition('@@') # ('foo.bar', '', '')

# rpartition()
# s is split at the last occurrence of <sep>
# instead of the first occurrence:
'foo@@bar@@baz'.rpartition('@@') # ('foo@@bar', '@@', 'baz')

# rsplit()
# Splits a string into a list of substrings
'foo bar baz qux'.rsplit() # ['foo', 'bar', 'baz', 'qux']
'foo\n\tbar   baz\r\fqux'.rsplit() # ['foo', 'bar', 'baz', 'qux']

# If <sep> is specified, it is used as the delimiter for splitting:
'foo.bar.baz.qux'.rsplit(sep='.') # ['foo', 'bar', 'baz', 'qux']

# If <sep> is explicitly given as a delimiter, 
# consecutive delimiters in s are assumed to delimit empty strings,
# which will be returned:
'foo...bar'.rsplit(sep='.') # ['foo', '', '', 'bar']

# Not the case if <sep> omitted:
'foo\t\t\tbar'.rsplit() # ['foo', 'bar']

# <maxsplit> defined:
'www.realpython.com'.rsplit(sep='.', maxsplit=1) # ['www.realpython', 'com']

# split()
# Splits are counted from the left end of s rather than the right end:
'www.realpython.com'.split('.', maxsplit=1) # ['www', 'realpython.com']

# If <maxsplit> is not specified, .split() and .rsplit() are indistinguishable.

# splitlines()
# Breaks a string at line boundaries
'foo\nbar\r\nbaz\fqux\u2028quux'.splitlines() # ['foo', 'bar', 'baz', 'qux', 'quux']
'foo\f\f\fbar'.splitlines() # ['foo', '', '', 'bar']

# If the optional <keepends> argument is specified and is truthy,
# then the lines boundaries are retained in the result strings:
'foo\nbar\nbaz\nqux'.splitlines(True) # ['foo\n', 'bar\n', 'baz\n', 'qux']

## Bytes


