# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# 1. CHAPTER
# 1.2. DECLARING FUNCTIONS
'''
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    Convert a file size to human-readable form.
    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
    if False, use multiples of 1000
    Returns: string

    if size < 0:
        raise ValueError('number must be non-negative')
        multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
        for suffix in SUFFIXES[multiple]:
            size /= multiple
            if size < multiple:
                    return '{0:.1f} {1}'.format(size, suffix)

        raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
'''

# 1.4. THE import SEARCH PATH
import sys
sys.path # sys.path is a list of directory names that constitute the current search path.
# ['', '/usr/lib/python31.zip', ...]

#1.5. EVERYTHING IS AN OBJECT
'''
Everything in Python is an object, and everything can have attributes and methods. 
All functions have a builtin attribute __doc__, which returns the docstring defined 
in the function’s source code. The sys module is
an object which has (among other things) an attribute called path. ...'''


# 1.6. INDENTING CODE
'''Indenting starts a block and unindenting ends it.'''
def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    if size < 0:
        raise ValueError('number must be non-negative')

#1.7. EXCEPTIONS
''' Like an error, an indication that something went wrong.
Exceptions can be handled

try...except blocks to handle exceptions,
    or
if size < 0:
    raise ValueError('number must be non-negative')
            --> Use the raise statement, followed by the exception
name, and an optional human-readable string for debugging purposes.
'''
#1.7.1. CATCHING IMPORT ERRORS
try:
    import chardet
except ImportError: # built-in exceptions -
# helps for example  when the module doesn’t exist in your import search path
    chardet = None

#1.9. EVERYTHING IS CASE-SENSITIVE

#1.10. RUNNING SCRIPTS

'''If you import the module, then
__name__ is the module’s filename, without a directory path or file extension.'''
import numpy
print(numpy.__name__)
'''__________________________________________________________________________________________'''

#CHAPTER 2. NATIVE DATATYPES
'''
1. Booleans are either True or False.
2. Numbers can be integers (1 and 2), floats (1.1 and 1.2), fractions (1/2 and 2/3), or even complex numbers.
3. Strings are sequences of Unicode characters, e.g. an HTML document.
4. Bytes and byte arrays, e.g. a JPEG image file.
5. Lists are ordered sequences of values.
6. Tuples are ordered, immutable sequences of values.
7. Sets are unordered bags of values.
8. Dictionaries are unordered bags of key-value pairs.
'''