#!/usr/bin/env python

import  sys

def main():
    print 'Hello there',sys.argv[1]

# Standard boilerplate to call the main function to begin.
if __name__ == '__main__':
    main()
# If a python module is run directly __name__ is set to __main__, and something else if it is not imported.
