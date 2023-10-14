#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None
for line in sys.stdin:
  line = line.strip()
  # Split on tab
  word, count = line.split('\t', 1)
  count = int(count)
  if current_word == word:
    # If we're on the current key, add to the count
    current_count += count
  else:
    if current_word:
      # Else if it's a new key start a new count
      print('%s:%s' % (current_word, current_count))
    current_count = count
    current_word = word
if current_word == word:
  print('%s:%s' % (current_word, current_count))