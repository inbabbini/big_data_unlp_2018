#!/usr/bin/env python
"""mapper.py"""

import sys

#read form STDIN
for line in sys.stdin:
	#parse per line
    group, number = line.strip().split() # clean line

    #print to STDOUT
    print "%s" % (number)