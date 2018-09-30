#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip() #clean line
    if line == "Muy satisfecho":
        print '%s\t%s' % (1, line)
    elif line == "Algo satisfecho":
        print '%s\t%s' % (2, line)
    elif line == "Poco satisfecho":
        print '%s\t%s' % (3, line)
    else: # line == "Muy disconforme"
        print '%s\t%s' % (4, line)