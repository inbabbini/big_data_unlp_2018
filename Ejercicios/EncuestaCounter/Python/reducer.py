#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_key = None
key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, word = line.split('\t')
    
    if key == current_key:
        current_count += 1
    else:
        if current_key != None:
            print "%s\t%s" % (current_key, current_count)
        current_key = key
        current_count = 1

if current_key == key:
    print "%s\t%s" % (current_key, current_count)