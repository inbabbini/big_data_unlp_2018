#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_number = None

# read from STDIN
for line in sys.stdin:
    read_number = line.strip() #clean line & read number

    if (current_number != read_number) do:
    	if (current_number != None) do:
    		print(current_number)
    	current_number = read_number

# print last number
print(current_number)