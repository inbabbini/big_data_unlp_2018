#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_number = None
current_count = 0

# read from STDIN
for line in sys.stdin:
    read_number = line.strip() #clean line & read number

    if (current_number != read_number):
    	if (current_number != None):
    		if (current_count < 3):
    			print("%s\t%i" % current_number, current_count)
    	current_number = read_number
    	current_count = 1
    else:
    	current_count += 1

# check last number
if (current_count == 1):
    print("X\t%s" % current_number)