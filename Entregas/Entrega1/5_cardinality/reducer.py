#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

count = 0

# read from STDIN
for line in sys.stdin:
    line = line.strip() #clean line
    key, quantity = line.split('\t')
    count += int(quantity)

print(count)