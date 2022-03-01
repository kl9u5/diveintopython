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



