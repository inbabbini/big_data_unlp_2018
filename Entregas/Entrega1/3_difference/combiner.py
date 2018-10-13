#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_number = None
current_count = 0
current_groups = []

# read from STDIN
for line in sys.stdin:
    line = line.strip() #clean line
    read_number, read_group = line.split('\t')

    if (current_number != read_number):
    	if (current_number != None) and (len(current_groups) < 2):
    		print("%s\t%s" % current_number, current_groups[0])
    	current_number = read_number
    	current_groups = [read_group]
    else:
    	current_groups.append(read_group)

# print last number
if (len(current_groups) < 2):
	print(current_number)