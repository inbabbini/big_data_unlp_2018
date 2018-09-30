#!/usr/bin/env python
"""mapper.py"""

import sys

#recover args
group = sys.argv[1]

#read form STDIN
for line in sys.stdin:
	#parse per line
    number = line.strip() # clean line

    #print to STDOUT
    print "%s\t%s" % (group, number)