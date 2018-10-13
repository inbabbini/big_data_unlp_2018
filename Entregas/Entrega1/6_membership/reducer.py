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
    if (current_number != None):
      if (current_number == "-1"):
        for number in current_groups:
          print ("%s\t%s" % (number, "SI"))
      elif (len(current_groups) == 2):
        print ("%s\t%s" % (current_number, "SI"))
      elif (len(current_groups) == 1 and current_groups[0] == "E"):
        print ("%s\t%s" % (current_number, "NO"))
    current_number = read_number
    current_groups = [read_group]
  else:
    current_groups.append(read_group)

# print last number
if (len(current_groups) == 2 ):
  print ("%s\t%s" % (current_number, "SI"))
elif (len(current_groups) == 1 and current_groups[0] == "E"):
  print ("%s\t%s" % (current_number, "NO"))