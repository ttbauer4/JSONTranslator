#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
json-translator.py translates a column of text into json list format
'''

__author__ = 'Trenton Bauer'
__version__ = 'V1.0'
__maintainer__ = 'Trenton Bauer'
__contact__ = 'trenton.bauer@gmail.com'
__status__ = 'Production'

import time

i = print('\nEnter your list elements below (one per line) and hit Ctrl-D or Ctrl-Z then Enter (Windows) on a new line when done:\n')
arr = []

while True:
    try:
        i = input()
    except EOFError:
        break
    arr.append(i)

print('\n')
for x in arr:
    print('\"' + x + '\"', end=', ')
print('\n\n')