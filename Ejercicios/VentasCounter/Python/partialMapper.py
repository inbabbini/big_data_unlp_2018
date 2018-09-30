#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip() # clean line
    branch, product, amount = line.split('\t') # recover values

    print "%s\t%s\t%s" % (product, branch, amount) #order by product