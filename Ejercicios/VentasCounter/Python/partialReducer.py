#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

# setup counters
current_branch = None
current_product = None
current_amount = 0

# process lines
for line in sys.stdin:
    line = line.strip()
    product, branch, amount = line.split('\t')

    if product == current_product:
        current_count += amount
    else:
        if current_product != None:
            print "%s\t%s\t%s" % (current_product, current_branch, current_amount)
        current_product = product
        current_branch = branch
        current_amount = amount

    

# print last line
if current_key == key:
    print "%s\t%s\t%s" % (current_product, current_branch, current_amount)