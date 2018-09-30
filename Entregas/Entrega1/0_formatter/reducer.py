#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

# read from STDIN
for line in sys.stdin:
    line = line.strip() #clean line
    print(line) #print to STDOUT line as is ("group\tnumber")