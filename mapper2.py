#!/usr/bin/python

import sys
import re

line = sys.stdin.readline()
# pattern to check for all words with no whitespace in them
pattern = re.compile("[^\s]+")
while line:
  for word in pattern.findall(line):
    # loop through word and get all vowels
    vowel = ''.join(sorted(filter(lambda x: x in 'aeiouy', word.lower())))
    print('{0}\t1'.format(vowel))
  line = sys.stdin.readline() 