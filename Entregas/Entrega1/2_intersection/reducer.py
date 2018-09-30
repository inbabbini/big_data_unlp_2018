#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_number = None
current_count = 0

# read from STDIN
for line in sys.stdin:
    read_number = line.strip() #clean line & read number

    if (current_number != read_number) do:
    	if (current_number != None) && (current_count > 1) do:
    		print(current_number)
    	current_number = read_number
    	current_count = 1
    else:
    	current_count++

# print last number
if (current_count > 1):
	print(current_number)