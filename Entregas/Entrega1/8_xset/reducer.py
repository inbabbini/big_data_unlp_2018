#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_number = None
current_count = 0

# read from STDIN
for line in sys.stdin:
    read_number, read_count = line.strip().split("\t") #clean line & read number

    if (current_number != read_number):
    	if (current_number != None) and (current_count == 1):
    		print("X\t%s" % current_number)
    	current_number = read_number
    	current_count = int(read_count)
    else:
    	current_count += int(read_count)

# check last number
if (current_count == 1):
    print("X\t%s" % current_number)