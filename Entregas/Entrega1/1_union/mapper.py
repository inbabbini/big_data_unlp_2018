#!/usr/bin/env python
"""mapper.py"""

import sys

# read form STDIN
for line in sys.stdin:
	# parse per line
    line = line.strip() # clean line
    group, number = line.split('\t')

    # print to STDOUT
    print "%s" % (number)