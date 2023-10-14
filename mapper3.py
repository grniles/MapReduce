#!/usr/bin/env python

import sys

line = sys.stdin.readline()
while line:
  line = line.strip()
  currentPerson, value = line.split(':', 1)
  currentPerson = ''.join(currentPerson.split())
  value = value.strip()
  friends = value.split(' ')
  for friend in friends:
    if friend < currentPerson:
      first = friend
      second = currentPerson
    else:
      first = currentPerson
      second = friend
    print('%s %s\t%s' % (first, second, friends))
  line = sys.stdin.readline()